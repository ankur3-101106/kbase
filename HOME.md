# Knowledge Base Home (`HOME.md`)

Welcome to your central knowledge hub. This dashboard provides immediate access to all topical areas, capture workflows, operational procedures, and templates across mobile, desktop, and GitHub.

---

## ⚡ Quick Capture & Inbox

- **[📥 Open Inbox](inbox/README.md)** — Capture raw ideas, commands, URLs, and quick notes.
- **[⚡ Quick Capture Template](templates/quick-capture.md)** — Minimal format for <30-second mobile entry.
- **[📋 Weekly Inbox Review Checklist](procedures/checklists/weekly-inbox-review.md)** — Step-by-step triage guide.

> **Mobile Tip:** Open `inbox/`, create `YYYY-MM-DD-topic.md`, write your note, and save. Triage later during your weekly review.

---

## 📚 Knowledge Areas

Curated, reusable concepts, technical documentation, and domain knowledge.

### 🛡️ [Cybersecurity](knowledge/cybersecurity/README.md)
- **[Digital Forensics & Incident Response (DFIR)](knowledge/cybersecurity/README.md#dfir)**
  - [DFIR Investigation Fundamentals](knowledge/cybersecurity/dfir/dfir-investigation-fundamentals.md)
- **[Networking & Protocol Security](knowledge/cybersecurity/README.md#networking)**
- **[Web Application Security](knowledge/cybersecurity/README.md#web-security)**
- **[Penetration Testing & Offensive Security](knowledge/cybersecurity/README.md#penetration-testing)**
- **[Security Research & Vulnerability Analysis](knowledge/cybersecurity/README.md#security-research)**

### 💻 [Systems & Infrastructure](knowledge/systems/README.md)
- **[Arch Linux Administration](knowledge/systems/README.md#arch-linux)**
- **[Windows 11 Administration](knowledge/systems/README.md#windows)**
- **[Systems Networking](knowledge/systems/README.md#networking)**
- **[Virtualization & Containers](knowledge/systems/README.md#virtualization)**
- [Cross-Platform Notes & Environment Workflow](knowledge/systems/cross-platform-notes-workflow.md)

### 🎓 [Education & Academics](knowledge/education/README.md)
- **[Data Structures & Algorithms](knowledge/education/README.md#data-structures)**
  - [Core Data Structures Cheatsheet](knowledge/education/data-structures/core-data-structures-cheatsheet.md)
- **[Databases & Storage Engines](knowledge/education/README.md#databases)**
- **[Exam Preparation & Study Guides](knowledge/education/README.md#exam-preparation)**

### 🧩 [Programming & Engineering](knowledge/programming/README.md)
- Language references, idioms, design patterns, architecture notes, and code snippets.

### 📖 [Reference & Tooling](knowledge/reference/README.md)
- [Search and Retrieval Guide](knowledge/reference/search-and-retrieval-guide.md)
- CLI syntax, terminal shortcuts, cheatsheets, and format conventions.

### 👤 [Personal & Workflow](knowledge/personal/README.md)
- Personal workflows, setup logs, and productivity documentation.

---

## 🛠️ Operational Procedures & SOPs

Step-by-step, repeatable instructions for tasks, recoveries, and troubleshooting.

- **[Procedures Index](procedures/README.md)**
- **[Git Commit & Push Guide](COMMIT.md)** — Conventional commit standards, pre-commit checklist, and push commands.
- **[Sync & Conflict Resolution SOP](procedures/synchronization-and-conflict-resolution.md)** — Resolving Git rebases, merge conflicts, and locks across Windows, Arch Linux, and Android.
- **[Git Sync Troubleshooting](procedures/troubleshooting/git-sync-failures.md)** — Recovery from stale locks, non-fast-forward push rejections, and detached states.
- **[Weekly Inbox Review](procedures/checklists/weekly-inbox-review.md)** — Standard checklist for note triage.
- **[Notion & Docusaurus Migration Guide](procedures/migration/notion-docusaurus-migration.md)** — Incremental migration without duplicate authoritative copies.

---

## 📂 Projects & External Resources

- **[Active Projects](projects/README.md)** — High-level plans, architecture decisions, and project logs.
- **[External Resources](resources/README.md)** — Catalogs of books, articles, research papers, and technical specifications.
- **[Media & Attachments](attachments/README.md)** — Sanitized diagrams, screenshots, and visual reference assets.
- **[Archive](archive/README.md)** — Inactive, completed, or superseded notes preserved for historical reference.

---

## 📑 Note Authoring Templates

Copy any template from the [`templates/`](templates/README.md) directory to start a new note:

| Template | Primary Use Case |
| :--- | :--- |
| [`templates/quick-capture.md`](templates/quick-capture.md) | Mobile/desktop rapid capture in under 30 seconds |
| [`templates/knowledge-note.md`](templates/knowledge-note.md) | Evergreen concept, reference note, or technology explanation |
| [`templates/troubleshooting-record.md`](templates/troubleshooting-record.md) | Problem diagnosis, symptoms, root cause, and verified fix |
| [`templates/cybersecurity-lab.md`](templates/cybersecurity-lab.md) | Hands-on security lab exercise with scope and findings |
| [`templates/dfir-investigation.md`](templates/dfir-investigation.md) | Incident investigation or post-mortem case study |
| [`templates/study-note.md`](templates/study-note.md) | Academic course topic, concept review, and exam prep |
| [`templates/sop-procedure.md`](templates/sop-procedure.md) | Step-by-step repeatable standard operating procedure |
| [`templates/project-overview.md`](templates/project-overview.md) | Project plan, architecture, milestones, and task tracking |
| [`templates/resource-summary.md`](templates/resource-summary.md) | Book, article, or research paper summary and takeaways |
| [`templates/decision-record.md`](templates/decision-record.md) | Architecture / Technical Decision Record (ADR) |

---

## 🧭 How to Work with This Knowledge Base

### 1. Creating a New Note
1. Select the appropriate template from [`templates/`](templates/README.md).
2. Choose a descriptive, hyphenated lowercase filename: `topic-subtopic.md` (e.g., `btrfs-subvolume-snapshots.md`).
3. Fill in the YAML frontmatter (defined in [`CONTRIBUTING.md`](CONTRIBUTING.md)).
4. Place the note in the appropriate category under `knowledge/`, `procedures/`, or `projects/`.

### 2. Finding Information
- **Ripgrep (CLI):** `rg -i "search phrase"`
- **Heading Search:** `rg "^#+ .*term"`
- **Metadata Search:** `rg "^type: procedure"` or `rg "^area: cybersecurity"`
- **GitHub UI:** Press `t` in the repository on GitHub to jump to any file, or use the search box with `path:knowledge/`.

### 3. Archiving Outdated Material
When a note is superseded or no longer active:
1. Update its frontmatter: `status: archived`.
2. Move the file into `archive/` (optionally retaining subfolder prefix: `archive/2026-topic.md`).
3. Add a note at the top linking to any replacement note if applicable.

---

## 🔒 Security Reminder

Never store cleartext passwords, API keys, private tokens, or proprietary forensic dumps in this repository. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for data sanitization standards.
