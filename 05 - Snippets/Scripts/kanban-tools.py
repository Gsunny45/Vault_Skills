#!/usr/bin/env python3
"""
kanban-tools.py — CLI utility for Obsidian Kanban boards via REST API.

Connects to the Obsidian REST API plugin (port 27123) to list, inspect,
modify, and validate Kanban boards. All operations go through the vault's
REST API — Obsidian must be open with the REST API plugin enabled.

Uses the same config file as rest-api.ps1 (rest-config.json) for credentials.

Usage:
  python kanban-tools.py list                          List all Kanban boards
  python kanban-tools.py show "Board Name"             Show board summary
  python kanban-tools.py add "Board" --lane "To Do"    Add a card to a lane
      --card "Card text" [--date 2026-05-01] [--tag tag1] [--no-checkbox]
  python kanban-tools.py move "Board"                  Move card between lanes
      --card "Card text" --to "In Progress"
  python kanban-tools.py check "Board" --card "Text"   Mark a card complete
  python kanban-tools.py archive "Board"               Archive all completed cards
  python kanban-tools.py validate "Board"              Check board file syntax
  python kanban-tools.py stats "Board"                 Card counts per lane
  python kanban-tools.py overdue                       Show overdue cards across all boards
  python kanban-tools.py config                        Show connection status
"""

import json
import os
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, date
from pathlib import Path


# ─── Config ──────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent.resolve()
CONFIG_PATH = SCRIPT_DIR / "rest-config.json"


def load_config():
    """Load REST API config from rest-config.json (same file rest-api.ps1 uses)."""
    if not CONFIG_PATH.exists():
        print(f"Config not found at {CONFIG_PATH}")
        print("Run rest-api.ps1 config first to set up your API key.")
        sys.exit(1)
    with open(CONFIG_PATH) as f:
        cfg = json.load(f)
    return cfg.get("BaseUrl", "http://127.0.0.1:27123"), cfg.get("ApiKey", "")


def api_request(method, endpoint, data=None):
    """Make an HTTP request to the Obsidian REST API."""
    base_url, api_key = load_config()
    url = f"{base_url}{endpoint}"
    headers = {"Authorization": api_key}
    if data is not None:
        headers["Content-Type"] = "application/json"
        body = json.dumps(data).encode("utf-8")
    else:
        body = None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"API error {e.code}: {e.read().decode()}")
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Connection failed — is Obsidian open with REST API plugin enabled?")
        print(f"  {e.reason}")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: API response was not valid JSON.")
        sys.exit(1)


def vault_list():
    """List all files in the vault root."""
    return api_request("GET", "/vault/")


def read_file(path):
    """Read a file from the vault."""
    import urllib.parse
    encoded = urllib.parse.quote(path, safe="")
    result = api_request("GET", f"/vault/{encoded}")
    if isinstance(result, dict) and "content" in result:
        return result["content"]
    return str(result)


def write_file(path, content):
    """Write content to a vault file."""
    import urllib.parse
    encoded = urllib.parse.quote(path, safe="")
    api_request("PUT", f"/vault/{encoded}", {"content": content})


def find_kanban_boards():
    """Find all markdown files with kanban-plugin frontmatter."""
    files = vault_list()
    if isinstance(files, dict) and "files" in files:
        files = files["files"]
    boards = []
    for f in files:
        if f.get("type") == "file" and f.get("name", "").endswith(".md"):
            try:
                content = read_file(f["name"])
                if "kanban-plugin:" in content.split("---", 2)[1] if content.count("---") >= 2 else False:
                    boards.append(f["name"])
            except (IndexError, Exception):
                continue
    return boards


# ─── Board Parser ────────────────────────────────────────────────────────────

class KanbanCard:
    """Represents a single card on a Kanban board."""
    def __init__(self, raw_line, checked=False, title="", date_str=None, tags=None, body=""):
        self.raw_line = raw_line
        self.checked = checked
        self.title = title
        self.date_str = date_str
        self.tags = tags or []
        self.body = body

    def __repr__(self):
        mark = "x" if self.checked else " "
        date_part = f" @{{{self.date_str}}}" if self.date_str else ""
        tags_part = " " + " ".join(f"#{t}" for t in self.tags) if self.tags else ""
        return f"[{mark}] {self.title}{date_part}{tags_part}"

    @property
    def is_overdue(self):
        """Check if card date is before today."""
        if not self.date_str:
            return False
        try:
            card_date = datetime.strptime(self.date_str, "%Y-%m-%d").date()
            return card_date < date.today()
        except ValueError:
            return False


class KanbanBoard:
    """Parsed representation of a Kanban board file."""

    CARD_RE = re.compile(
        r"^\s*-\s+\[([ xX])\]\s+(.*?)(?:@\{(\d{4}-\d{2}-\d{2})\})?\s*(.*?)$"
    )
    TAG_RE = re.compile(r"#([\w/-]+)")
    LANE_RE = re.compile(r"^##\s+(.+)$")
    ARCHIVE_SEP_RE = re.compile(r"^\*\*\*$")
    SETTINGS_RE = re.compile(r"%%\s*kanban:settings")

    def __init__(self, path, content):
        self.path = path
        self.content = content
        self.lanes = []          # list of (lane_name, [card, ...])
        self.archive = []        # list of cards in archive
        self.settings_block = "" # raw settings JSON
        self.error = None
        self._parse(content)

    def _parse(self, content):
        lines = content.split("\n")
        # Strip frontmatter
        if lines and lines[0].strip() == "---":
            try:
                end = lines.index("---", 1)
                lines = lines[end + 1:]
            except ValueError:
                self.error = "Unclosed frontmatter block"
                return

        current_lane = None
        current_cards = []
        in_archive = False
        in_settings = False
        archive_cards = []
        settings_lines = []

        for line in lines:
            stripped = line.strip()

            # Skip settings block
            if self.SETTINGS_RE.search(stripped):
                in_settings = True
                settings_lines = [line]
                continue
            if in_settings:
                settings_lines.append(line)
                if stripped.endswith("%%"):
                    self.settings_block = "\n".join(settings_lines)
                    in_settings = False
                continue

            # Archive separator
            if self.ARCHIVE_SEP_RE.match(stripped):
                if current_lane and current_cards:
                    self.lanes.append((current_lane, current_cards))
                current_lane = None
                current_cards = []
                in_archive = True
                continue

            # Lane header
            lane_match = self.LANE_RE.match(stripped)
            if lane_match:
                if current_lane and current_cards:
                    entry = (current_lane, current_cards)
                    if in_archive:
                        archive_cards.extend(current_cards)
                    else:
                        self.lanes.append(entry)
                current_lane = lane_match.group(1).strip()
                current_cards = []
                continue

            # Card line
            card_match = self.CARD_RE.match(stripped)
            if card_match:
                checked_char = card_match.group(1)
                title = card_match.group(2).strip()
                date_str = card_match.group(3)
                rest = card_match.group(4).strip()
                tags = self.TAG_RE.findall(title + " " + rest)
                checked = checked_char in ("x", "X")
                card = KanbanCard(
                    raw_line=stripped,
                    checked=checked,
                    title=title,
                    date_str=date_str,
                    tags=tags,
                    body=rest
                )
                current_cards.append(card)
                continue

            # Body continuation (indented line after a card)
            if current_cards and stripped and line.startswith(("  ", "\t")):
                current_cards[-1].body += "\n" + stripped

        # Flush last lane
        if current_lane and current_cards:
            if in_archive:
                archive_cards.extend(current_cards)
            else:
                self.lanes.append((current_lane, current_cards))
        self.archive = archive_cards


# ─── Commands ────────────────────────────────────────────────────────────────

def cmd_config():
    """Show connection status."""
    base_url, api_key = load_config()
    key_preview = api_key[:20] + "..." if len(api_key) > 20 else api_key
    print(f"REST API URL: {base_url}")
    print(f"API Key:     {key_preview}")
    try:
        info = api_request("GET", "/")
        print(f"Vault:       {info.get('vault_name', 'unknown')}")
        print(f"Files:       {info.get('file_count', '?')}")
        print("Status:      Connected")
    except Exception:
        print("Status:      Connection failed")


def cmd_list():
    """List all Kanban boards in the vault."""
    boards = find_kanban_boards()
    if not boards:
        print("No Kanban boards found.")
        return
    print(f"Found {len(boards)} Kanban board(s):\n")
    for b in boards:
        content = read_file(b)
        board = KanbanBoard(b, content)
        card_count = sum(len(cards) for _, cards in board.lanes)
        lane_count = len(board.lanes)
        archive_count = len(board.archive)
        print(f"  {b}")
        print(f"    {lane_count} lanes, {card_count} cards, {archive_count} archived")
        # Show overdue count
        overdue = sum(1 for _, cards in board.lanes for c in cards if c.is_overdue)
        if overdue:
            print(f"    ⚠ {overdue} overdue card(s)")


def cmd_show(board_name):
    """Show detailed board summary."""
    path = _resolve_board(board_name)
    content = read_file(path)
    board = KanbanBoard(path, content)
    print(f"\nBoard: {path}")
    print(f"{'─' * 60}")
    for lane_name, cards in board.lanes:
        icon = "✅" if "complete" in lane_name.lower() else "⬜"
        print(f"\n  {icon} {lane_name} ({len(cards)} cards)")
        for c in cards:
            overdue_mark = " ⚠ OVERDUE" if c.is_overdue else ""
            print(f"    {'[x]' if c.checked else '[ ]'} {c.title}{overdue_mark}")
            if c.date_str:
                print(f"         Due: {c.date_str}")
            if c.tags:
                print(f"         Tags: {', '.join(c.tags)}")
            if c.body and c.body != c.tags:
                body_preview = c.body[:60] + "..." if len(c.body) > 60 else c.body
                print(f"         {body_preview}")
    if board.archive:
        print(f"\n  📦 Archive ({len(board.archive)} cards)")
    print()


def cmd_add(board_name, lane_name, card_text, date_str=None, tags=None, no_checkbox=False):
    """Add a card to a specific lane."""
    path = _resolve_board(board_name)
    content = read_file(path)
    board = KanbanBoard(path, content)

    # Find the target lane
    target_idx = None
    for i, (ln, _) in enumerate(board.lanes):
        if ln.lower() == lane_name.lower():
            target_idx = i
            break
    if target_idx is None:
        print(f"Error: Lane '{lane_name}' not found.")
        print(f"Available lanes: {', '.join(ln for ln, _ in board.lanes)}")
        sys.exit(1)

    # Build card line
    checkbox = "" if no_checkbox else "[ ] "
    date_part = f" @{{{date_str}}}" if date_str else ""
    tags_part = " " + " ".join(f"#{t}" for t in tags) if tags else ""
    card_line = f"- {checkbox}**{card_text}**{date_part}{tags_part}"

    # Find insertion point in original content
    lines = content.split("\n")
    lane_header = f"## {board.lanes[target_idx][0]}"
    insert_idx = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == lane_header:
            # Insert after the lane header and any blank lines after it
            insert_idx = i + 1
            while insert_idx < len(lines) and lines[insert_idx].strip() == "":
                insert_idx += 1
            break

    if insert_idx is None:
        print(f"Error: Could not find lane header in file.")
        sys.exit(1)

    lines.insert(insert_idx, card_line)
    write_file(path, "\n".join(lines))
    print(f"Added card to '{lane_name}': {card_text}")


def cmd_move(board_name, card_text, target_lane):
    """Move a card from its current lane to another lane."""
    path = _resolve_board(board_name)
    content = read_file(path)
    board = KanbanBoard(path, content)

    # Find the card
    found_card = None
    source_lane = None
    source_idx = None
    for lane_idx, (ln, cards) in enumerate(board.lanes):
        for card_idx, c in enumerate(cards):
            if card_text.lower() in c.title.lower():
                found_card = c
                source_lane = ln
                source_lane_idx = lane_idx
                source_card_idx = card_idx
                break
        if found_card:
            break

    if not found_card:
        print(f"Error: Card matching '{card_text}' not found.")
        sys.exit(1)

    # Find target lane
    target_idx = None
    for i, (ln, _) in enumerate(board.lanes):
        if ln.lower() == target_lane.lower():
            target_idx = i
            break
    if target_idx is None:
        print(f"Error: Target lane '{target_lane}' not found.")
        sys.exit(1)

    # Get original lines
    lines = content.split("\n")

    # Find and remove the card line
    source_header = f"## {source_lane}"
    target_header = f"## {board.lanes[target_idx][0]}"

    card_line_idx = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == found_card.raw_line:
            card_line_idx = i
            break

    if card_line_idx is None:
        # Try fuzzy match on title
        for i, line in enumerate(lines):
            if card_text.lower() in line.lower():
                card_line_idx = i
                break

    if card_line_idx is None:
        print("Error: Could not find card line in file content.")
        sys.exit(1)

    # Remove card line
    card_line = lines.pop(card_line_idx)

    # Find insertion point in target lane
    insert_idx = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == target_header:
            insert_idx = i + 1
            while insert_idx < len(lines) and lines[insert_idx].strip() == "":
                insert_idx += 1
            break

    if insert_idx is not None:
        lines.insert(insert_idx, card_line)
        write_file(path, "\n".join(lines))
        print(f"Moved card from '{source_lane}' to '{target_lane}': {card_text}")
    else:
        print(f"Error: Could not find target lane in file.")
        sys.exit(1)


def cmd_check(board_name, card_text):
    """Mark a card as complete (set [x])."""
    path = _resolve_board(board_name)
    content = read_file(path)
    board = KanbanBoard(path, content)

    lines = content.split("\n")
    found = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if card_text.lower() in stripped.lower() and re.match(r"^\s*- \[ \]", stripped):
            lines[i] = stripped.replace("- [ ]", "- [x]", 1)
            found = True
            print(f"Marked complete: {stripped.strip()}")
            break

    if found:
        write_file(path, "\n".join(lines))
    else:
        print(f"Card matching '{card_text}' not found or already checked.")


def cmd_archive(board_name):
    """Move all checked cards from **Complete lane to Archive section."""
    path = _resolve_board(board_name)
    content = read_file(path)
    board = KanbanBoard(path, content)

    lines = content.split("\n")

    # Find which lane is the Complete lane
    complete_lane = None
    for ln, cards in board.lanes:
        if "complete" in ln.lower():
            complete_lane = ln
            break

    if not complete_lane:
        print("No **Complete lane found. Nothing to archive.")
        return

    completed_header = f"## {complete_lane}"
    archive_header = "## Archive"
    separator = "***"

    # Find checked cards in the Complete lane content
    in_complete = False
    checked_cards = []
    complete_lane_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped == completed_header:
            in_complete = True
            complete_lane_lines = [line]
            continue
        if in_complete:
            if stripped.startswith("## ") or stripped == separator:
                in_complete = False
                continue
            complete_lane_lines.append(line)
            if re.match(r"^\s*- \[x\]", stripped):
                checked_cards.append(line)

    if not checked_cards:
        print("No checked cards found in Complete lane.")
        return

    # Find archive position or create it
    archive_idx = None
    for i, line in enumerate(lines):
        if line.strip() == archive_header:
            archive_idx = i + 1
            while archive_idx < len(lines) and lines[archive_idx].strip() == "":
                archive_idx += 1
            break

    # If no archive section, add it at the end
    if archive_idx is None:
        # Find the archive separator
        sep_idx = None
        for i, line in enumerate(lines):
            if line.strip() == separator:
                sep_idx = i
                break
        if sep_idx is None:
            lines.append("")
            lines.append(separator)
            lines.append("")
            lines.append(archive_header)
            lines.append("")
            archive_idx = len(lines)
        else:
            lines.insert(sep_idx + 1, "")
            lines.insert(sep_idx + 2, archive_header)
            lines.insert(sep_idx + 3, "")
            archive_idx = sep_idx + 4

    # Remove checked cards from their positions in Complete lane
    removed_count = 0
    new_lines = []
    for line in lines:
        if line in checked_cards:
            checked_cards.remove(line)
            # Add to archive
            new_lines.insert(archive_idx, line.rstrip())
            archive_idx += 1
            removed_count += 1
        else:
            new_lines.append(line)

    # Add archive separator before archived cards if it doesn't exist
    final_content = "\n".join(new_lines)
    write_file(path, final_content)
    print(f"Archived {removed_count} card(s).")


def cmd_validate(board_name):
    """Validate a board file for common issues."""
    path = _resolve_board(board_name)
    content = read_file(path)
    board = KanbanBoard(path, content)
    issues = []

    # Check frontmatter
    if not content.startswith("---"):
        issues.append("MISSING FRONTMATTER — file must start with `---`")
    else:
        try:
            end = content.index("---", 3)
            fm = content[3:end]
            if "kanban-plugin:" not in fm:
                issues.append("MISSING `kanban-plugin:` in frontmatter")
            if "kanban-plugin: board" not in fm and "kanban-plugin: basic" not in fm:
                issues.append("UNKNOWN kanban-plugin value — use `board` or `basic`")
        except ValueError:
            issues.append("UNCLOSED FRONTMATTER — no closing `---`")

    # Check lanes
    if not board.lanes:
        issues.append("NO LANES — board must have at least one `## Lane Name` header")

    # Check for Complete lane
    has_complete = any("complete" in ln.lower() for ln, _ in board.lanes)
    if not has_complete:
        issues.append("NO **COMPLETE LANE — missing auto-complete on drag-drop")

    # Check archive
    has_archive_sep = "***" in content
    if not has_archive_sep:
        issues.append("NO ARCHIVE SEPARATOR — missing `***` before Archive section")

    # Check cards for common issues
    wrong_dates = 0
    no_tags = 0
    total_cards = 0
    for _, cards in board.lanes:
        for c in cards:
            total_cards += 1
            if not c.date_str:
                no_tags += 1
            # Check for Due: syntax (wrong)
            if "due:" in c.title.lower() or "due:" in c.body.lower():
                wrong_dates += 1

    if wrong_dates:
        issues.append(f"WRONG DATE SYNTAX — {wrong_dates} card(s) use `Due:` instead of `@{{YYYY-MM-DD}}`")
    if no_tags == total_cards and total_cards > 0:
        issues.append("NO TAGS — consider adding `#tags` to cards for filtering")

    # Print results
    print(f"\nValidation: {path}")
    print(f"{'─' * 60}")
    if not issues:
        print("✅ No issues found.")
    else:
        for issue in issues:
            print(f"  ⚠  {issue}")
        print(f"\n  {len(issues)} issue(s) found.")
    print(f"  {len(board.lanes)} lanes, {total_cards} cards, {len(board.archive)} archived")
    print()


def cmd_stats(board_name):
    """Show card statistics for a board."""
    path = _resolve_board(board_name)
    content = read_file(path)
    board = KanbanBoard(path, content)

    total = sum(len(cards) for _, cards in board.lanes)
    checked = sum(1 for _, cards in board.lanes for c in cards if c.checked)
    unchecked = total - checked
    overdue = sum(1 for _, cards in board.lanes for c in cards if c.is_overdue)
    tagged = sum(1 for _, cards in board.lanes for c in cards if c.tags)

    print(f"\n📊 Stats: {board.path}")
    print(f"{'─' * 40}")
    print(f"  Lanes:     {len(board.lanes)}")
    print(f"  Cards:     {total} ({unchecked} open, {checked} done)")
    print(f"  Archived:  {len(board.archive)}")
    print(f"  Overdue:   {overdue}")
    print(f"  Tagged:    {tagged}/{total}")
    print()
    for lane_name, cards in board.lanes:
        done = sum(1 for c in cards if c.checked)
        ov = sum(1 for c in cards if c.is_overdue)
        ov_mark = " ⚠" if ov else ""
        print(f"  {lane_name}: {len(cards)} cards ({done} done{ov_mark})")
    print()


def cmd_overdue():
    """Show all overdue cards across all boards."""
    boards = find_kanban_boards()
    found_any = False
    today = date.today()

    for path in boards:
        content = read_file(path)
        board = KanbanBoard(path, content)
        overdue_cards = []
        for lane_name, cards in board.lanes:
            for c in cards:
                if c.is_overdue:
                    overdue_cards.append((lane_name, c))

        if overdue_cards:
            found_any = True
            print(f"\n📋 {path}")
            for lane_name, c in overdue_cards:
                print(f"  [{lane_name}] {c.title} @{{{c.date_str}}}")
                days_over = (today - datetime.strptime(c.date_str, "%Y-%m-%d").date()).days
                print(f"           {days_over} day(s) overdue")
                if c.tags:
                    print(f"           Tags: {', '.join(c.tags)}")

    if not found_any:
        print("No overdue cards found. 🎉")


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _resolve_board(name):
    """Resolve a board name or partial path to a full vault path."""
    boards = find_kanban_boards()
    if not boards:
        print("No Kanban boards found in vault.")
        sys.exit(1)

    # Exact match
    for b in boards:
        if b == name or Path(b).stem == name:
            return b

    # Partial match
    matches = [b for b in boards if name.lower() in b.lower()]
    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        print(f"Multiple boards match '{name}':")
        for m in matches:
            print(f"  {m}")
        sys.exit(1)

    print(f"Board '{name}' not found. Available boards:")
    for b in boards:
        print(f"  {b}")
    sys.exit(1)


# ─── CLI Entry Point ─────────────────────────────────────────────────────────

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Manage Obsidian Kanban boards via REST API.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python kanban-tools.py list
  python kanban-tools.py show "Project Board"
  python kanban-tools.py add "Project Board" --lane "Next Up" --card "Fix login bug" --date 2026-05-15 --tag dev
  python kanban-tools.py move "Project Board" --card "Fix login bug" --to "In Progress"
  python kanban-tools.py check "Project Board" --card "Fix login bug"
  python kanban-tools.py archive "Project Board"
  python kanban-tools.py stats "Project Board"
  python kanban-tools.py validate "Project Board"
  python kanban-tools.py overdue
  python kanban-tools.py config
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # list
    p_list = subparsers.add_parser("list", help="List all Kanban boards")

    # show
    p_show = subparsers.add_parser("show", help="Show board details")
    p_show.add_argument("board", help="Board name or path")

    # add
    p_add = subparsers.add_parser("add", help="Add a card to a lane")
    p_add.add_argument("board", help="Board name or path")
    p_add.add_argument("--lane", required=True, help="Target lane name")
    p_add.add_argument("--card", required=True, help="Card text")
    p_add.add_argument("--date", help="Due date (YYYY-MM-DD)")
    p_add.add_argument("--tag", action="append", dest="tags", help="Tag (can be repeated)")
    p_add.add_argument("--no-checkbox", action="store_true", help="Omit checkbox prefix")

    # move
    p_move = subparsers.add_parser("move", help="Move a card between lanes")
    p_move.add_argument("board", help="Board name or path")
    p_move.add_argument("--card", required=True, help="Card title (partial match)")
    p_move.add_argument("--to", required=True, dest="target_lane", help="Target lane name")

    # check
    p_check = subparsers.add_parser("check", help="Mark a card complete")
    p_check.add_argument("board", help="Board name or path")
    p_check.add_argument("--card", required=True, help="Card title (partial match)")

    # archive
    p_archive = subparsers.add_parser("archive", help="Archive all completed cards")
    p_archive.add_argument("board", help="Board name or path")

    # validate
    p_validate = subparsers.add_parser("validate", help="Check board syntax")
    p_validate.add_argument("board", help="Board name or path")

    # stats
    p_stats = subparsers.add_parser("stats", help="Show card statistics")
    p_stats.add_argument("board", help="Board name or path")

    # overdue
    p_overdue = subparsers.add_parser("overdue", help="Show overdue cards across all boards")

    # config
    p_config = subparsers.add_parser("config", help="Show connection status")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Route commands
    commands = {
        "list": lambda: cmd_list(),
        "show": lambda: cmd_show(args.board),
        "add": lambda: cmd_add(args.board, args.lane, args.card, args.date, args.tags, args.no_checkbox),
        "move": lambda: cmd_move(args.board, args.card, args.target_lane),
        "check": lambda: cmd_check(args.board, args.card),
        "archive": lambda: cmd_archive(args.board),
        "validate": lambda: cmd_validate(args.board),
        "stats": lambda: cmd_stats(args.board),
        "overdue": lambda: cmd_overdue(),
        "config": lambda: cmd_config(),
    }

    commands[args.command]()


if __name__ == "__main__":
    main()
