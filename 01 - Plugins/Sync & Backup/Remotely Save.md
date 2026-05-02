---
type: plugin
name: Remotely Save
category: Sync & Backup
status: active
complexity: medium
downloads: 1.8M+
last-verified: 2026-04-30
tags:
  - plugin
  - sync
  - backup
  - cloud
  - s3
  - onedrive
  - dropbox
---

# Remotely Save

> Plugin by remotely-save — syncs your Obsidian vault to cloud storage without an Obsidian Sync subscription. Supports S3-compatible storage, Dropbox, OneDrive, WebDAV, and more.

## What It Does

Remotely Save is a free alternative to Obsidian Sync. It syncs vault files between devices by using a cloud storage backend you control. Unlike Obsidian Git (which tracks history), Remotely Save focuses on real-time bidirectional sync — making your vault available on every device automatically.

Supported backends:
- **S3-compatible** — Amazon S3, Cloudflare R2, Backblaze B2, MinIO (self-hosted)
- **Dropbox**
- **OneDrive** (personal and work accounts)
- **WebDAV** — Nextcloud, Owncloud, any WebDAV server
- **Box** (experimental)

Key features:
- **End-to-end encryption** (E2EE) — files are encrypted before upload with a passphrase
- **Sync on startup** — automatically syncs when Obsidian opens
- **Sync on interval** — periodic background sync
- **Conflict resolution** — configurable strategies for conflicting edits
- **Partial sync** — skip folders you don't want in the cloud

## When To Use It

- Syncing your vault between your Windows PC and Android phone
- Free alternative to Obsidian Sync ($10/month)
- You already use OneDrive or Dropbox and want to leverage existing storage
- Self-hosted setup (Nextcloud/WebDAV) for full data sovereignty
- Backup to cloud without git workflow overhead

**Use alongside Obsidian Git** — they serve different purposes. Git = version history + code-style workflow; Remotely Save = seamless cross-device sync.

## Minimal Setup

### Option A — OneDrive (easiest for Windows users, you already have it)
1. **Install**: Community Plugins → search "Remotely Save" → Install & Enable
2. Settings → Remotely Save → Service → OneDrive (Personal)
3. Click **Auth** → browser opens → sign in to Microsoft account
4. Click **Check** to verify connection
5. Set **Sync on startup** to On
6. Click **Sync** — first sync uploads your vault

### Option B — Cloudflare R2 (free tier, S3-compatible)
Cloudflare R2 gives 10GB free with no egress fees — ideal for vaults.

1. Create a Cloudflare account → R2 → Create bucket (e.g., `obsidian-vault`)
2. R2 → Manage R2 API Tokens → Create Token → "Edit" permissions on your bucket
3. Copy: Account ID, Access Key ID, Secret Access Key
4. In Remotely Save settings:
   - Service: S3
   - Endpoint: `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`
   - Region: `auto`
   - Bucket: `obsidian-vault`
   - Access Key ID / Secret: (from step 3)

### Option C — Dropbox
1. Settings → Remotely Save → Service → Dropbox
2. Click **Auth** → authorize via Dropbox OAuth
3. Files sync to `Dropbox/Apps/remotely-save/<vault-name>/`

## Key Settings

| Setting | Recommended Value | Notes |
|---|---|---|
| Service | OneDrive or S3/R2 | Your preferred backend |
| Sync on startup | On | Syncs when Obsidian opens |
| Sync interval (minutes) | `0` (disable) | Background sync; leave off unless you need live sync. Manual + startup is enough for most. |
| Encryption password | (set a strong passphrase) | Encrypts files before upload. Store this passphrase safely — losing it means losing access to your cloud backup. |
| Skip large files (MB) | `10` | Skips files larger than 10MB to avoid syncing large Excalidraw or media files |
| Excluded folders | `.obsidian/workspace.json` | Skip frequently-changing files that don't need sync |
| Conflict strategy | Local wins | In a conflict, your local edit takes precedence. Change to "Remote wins" if you trust the remote as authoritative. |
| Sync `_` prefixed files | Off | Obsidian system files |
| Delete remote files when deleted locally | On | Keeps remote in sync when you delete notes |

## Gotchas & Known Issues

- **Not a replacement for version history** — Remotely Save overwrites previous versions on the remote. You can't roll back to yesterday's version of a note. Use Obsidian Git for version history.
- **Encryption passphrase must match on all devices** — if you set a passphrase on one device, you must enter the exact same passphrase on every other device. Mismatches cause sync failures that look like empty vaults.
- **Large vaults on first sync are slow** — syncing 10,000+ files for the first time can take 10-30 minutes. Let it run to completion before editing.
- **Conflict resolution is file-level** — there's no line-level merge. A conflict results in one version winning; the other is saved with a conflict suffix. Review these files periodically.
- **OneDrive rate limits** — Microsoft's API has rate limits. If you sync too frequently (short interval), you may hit throttling. Sync on startup + manual sync is more reliable.
- **Plugin doesn't sync `.obsidian/plugins/`** — community plugin binaries aren't synced. Re-install plugins on each device separately. Only your notes and settings files sync.
- **Disk space**: you only have ~24GB free. Monitor vault size before enabling cloud sync of media-heavy vaults.

## Works Well With

- [[Obsidian Git]] — Git for version history; Remotely Save for device sync. Use both.
- [[Excalidraw]] — configure Skip large files to avoid syncing huge drawing files if not needed on all devices

## Related Skills

- [[Vault Architecture]]

## Links

- [GitHub](https://github.com/remotely-save/remotely-save)
- [Obsidian Plugin Page](https://obsidian.md/plugins?id=remotely-save)
