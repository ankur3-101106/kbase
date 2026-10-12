# Knowledge Archive (`archive/`)

The archive preserves superseded notes, completed projects, deprecated SOPs, and historical records.

---

## 📌 Archiving Policy

Notes are never silently deleted unless they were transient scratch notes in `inbox/`. Authoritative notes that become obsolete are archived:

1. **Update Frontmatter:** Set `status: archived` and update `updated: YYYY-MM-DD`.
2. **Add Superseded Banner:** If a newer note replaces it, add a link at the top:
   ```markdown
   > [!NOTE]
   > This document was archived on 2026-10-12.
   > Superseded by [New Document Name](../knowledge/path/new-doc.md).
   ```
3. **Move to Archive:** Move the file into `archive/` (optionally prepending the archive year: `archive/YYYY-old-note.md`).
4. **Preserve Git History:** Moving via Git preserves all commit and blame history.
