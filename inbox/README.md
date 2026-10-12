# Inbox (`inbox/`)

The inbox is the zero-friction landing zone for unrefined ideas, quick terminal snippets, article links, meeting notes, or fleeting thoughts captured while on mobile or working quickly.

---

## ⚡ The 30-Second Mobile Capture Workflow

When capturing a thought on Android (via Markor, Termux, or any text editor):

1. **Create a file** in `inbox/` using the naming pattern:
   ```text
   YYYY-MM-DD-short-topic.md
   ```
   *(Example: `2026-10-12-btrfs-scrub-command.md`)*
2. **Copy or type the minimal capture format:**
   ```markdown
   # Quick Note: <Title>

   Captured: 2026-10-12

   ## Information
   Write your thought, command, error message, or snippet here.

   ## Source
   - URL:

   ## Follow-up
   - [ ] Triage and file this note
   ```
3. **Save and close.** Do not spend time filling out full metadata or organizing folders on mobile.
4. The background synchronization script (`kbase-sync.sh`) will commit and push the file during the next scheduled sync.

---

## 🧹 Triage & Filing Workflow

During your regular review (see [`procedures/checklists/weekly-inbox-review.md`](../procedures/checklists/weekly-inbox-review.md)):

1. Open the note in your desktop editor.
2. Decide its permanent category:
   - **Reusable concept or reference?** ➡️ Move to `knowledge/<area>/<topic>.md`
   - **Actionable, repeatable process or SOP?** ➡️ Move to `procedures/<category>/<topic>.md`
   - **Diagnosis of a bug or failure?** ➡️ Move to `procedures/troubleshooting/<topic>.md`
   - **Active project task or architecture decision?** ➡️ Move to `projects/<project-name>/`
   - **Superficial, temporary, or already resolved?** ➡️ Delete or move to `archive/`
3. Add appropriate YAML frontmatter (see [`CONTRIBUTING.md`](../CONTRIBUTING.md)).
4. Remove the raw file from `inbox/`.

> [!TIP]
> The goal is to keep `inbox/` near empty. An empty inbox means your knowledge base is organized and reliable.
