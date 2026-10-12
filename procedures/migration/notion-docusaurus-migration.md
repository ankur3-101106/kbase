---
title: "Procedure: Incremental Migration from Notion & Docusaurus"
type: procedure
area: procedures
topics:
  - migration
  - notion
  - docusaurus
status: evergreen
created: 2026-10-12
updated: 2026-10-12
---

# Procedure: Incremental Migration from Notion & Docusaurus

## 1. Migration Strategy & Core Principles

To prevent repository bloat, stale notes, and merge conflicts, follow these strict principles when importing content from previous Notion workspaces or the Docusaurus documentation site (`ankur3-101106.github.io`):

1. **No Bulk Imports:** Never export an entire Notion workspace or Docusaurus repository and dump it unreviewed into `kbase`. Bulk imports bring in stale files, broken links, non-standard HTML tags, and duplicate data.
2. **Single Authoritative Copy:** Avoid having two active editable copies of the same note. Decide clearly:
   - **Internal / Working Knowledge Base:** Belongs in `kbase` (authoritative source).
   - **Publicly Published Documentation:** Belongs in the Docusaurus repository (`ankur3-101106.github.io`). If an article is published publicly, `kbase` holds either the source draft or a reference link.
3. **Curate and Refactor:** Migrate notes on a per-topic basis only when you actively need or reference them. Convert each note to the proper template and taxonomy.
4. **Strict Sanitization:** Notion pages often contain personal notes, credentials, student IDs, or keys. Review every note for secrets before committing to Git.

---

## 2. Topic Mapping Matrix

| Existing Source Material (Docusaurus / Notion) | Target `kbase` Directory | Note Type (`type`) | Recommended Template |
| :--- | :--- | :--- | :--- |
| **`Sem-4` University Notes** | `knowledge/education/` | `study-note` | [`templates/study-note.md`](../../templates/study-note.md) |
| **`Sem-5` University Notes** | `knowledge/education/` | `study-note` | [`templates/study-note.md`](../../templates/study-note.md) |
| **Hacks / Security Tricks** | `knowledge/cybersecurity/` or `knowledge/systems/` | `reference` | [`templates/knowledge-note.md`](../../templates/knowledge-note.md) |
| **System Configurations** | `procedures/troubleshooting/` or `knowledge/systems/` | `procedure` | [`templates/sop-procedure.md`](../../templates/sop-procedure.md) |
| **SEO Master Guide** | `resources/documentation/` | `resource` | [`templates/resource-summary.md`](../../templates/resource-summary.md) |
| **Personal Projects** | `projects/<project-name>/` | `project` | [`templates/project-overview.md`](../../templates/project-overview.md) |
| **Raw Fleeting Notes** | `inbox/` | `capture` | [`templates/quick-capture.md`](../../templates/quick-capture.md) |

---

## 3. Step-by-Step Migration Checklist

### Step 1: Select and Extract
1. Identify a specific high-value note or subtopic to migrate (e.g., *Sem-5 Database Normalization*).
2. Export the note as Markdown or copy its raw text.
3. If the note includes images, save them into `attachments/` with a descriptive, lowercase name (e.g., `attachments/db-bcnf-decomposition.png`).

### Step 2: Clean and Normalize
1. Apply the appropriate template from `templates/`.
2. Fill in the YAML frontmatter:
   ```yaml
   ---
   title: Database Normalization (1NF to BCNF)
   type: study-note
   area: education
   topics:
     - databases
     - exam-prep
   status: active
   created: 2026-10-12
   updated: 2026-10-12
   source: "Sem-5 Academic Notes"
   ---
   ```
3. Strip any proprietary Notion export IDs from filenames (e.g., remove trailing UUIDs like `Database-Normalization-a1b2c3d4.md` ➡️ `database-normalization.md`).
4. Replace raw HTML blocks (like `<details>`, `<kbd>`, `<font>`) with clean Markdown where possible.

### Step 3: Sanitize Secrets
Audit the file for:
- [ ] Passwords, API keys, or tokens.
- [ ] School portal passwords or internal IP addresses.
- [ ] Personal confidential information.
Replace any occurrences with `<REDACTED>` or documentation ranges.

### Step 4: Validate and Verify
1. Run local validation:
   ```bash
   python tools/validate.py
   ```
2. Confirm links resolve and frontmatter is valid.
3. Commit and let the daily sync propagate the note across all devices.
