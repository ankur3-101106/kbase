# Personal Knowledge Base (`kbase`)

> A local-first, plain-text, cross-platform personal knowledge base engineered for longevity, zero-dependency readability, and multi-device Git synchronization.

---

## 1. Overview & Philosophy

`kbase` is a centralized repository of technical knowledge, operational procedures, study material, research notes, and project records. It is designed to be completely offline-first, portable, and durable over decades.

- **Plain Markdown First:** Notes are plain UTF-8 text files formatted with standard CommonMark / GitHub Flavored Markdown. No proprietary database, custom binary storage, or Electron app is required to read or write notes.
- **Local-First & Offline:** Notes live on local storage across devices. Note authoring, search, and reading function 100% offline.
- **Cross-Platform:** Actively operated across **Windows 11** (Git Bash), **Arch Linux** (Bash), **Android** (Termux & mobile Markdown editors like Markor), and **GitHub**.
- **Shallow Hierarchy & Portability:** Directories are lowercase and shallow (max 3–4 levels), filenames are descriptive and hyphenated (`kebab-case.md`), and internal links use standard relative Markdown paths (`[Title](../path/to/note.md)`).
- **Decoupled Tooling:** Optional validation tools and search helpers exist to assist maintenance, but zero runtimes (Node.js, Python, databases) are required for daily knowledge work.

---

## 2. Quick Navigation

| Document                                  | Purpose                                                                                                           |
| :---------------------------------------- | :---------------------------------------------------------------------------------------------------------------- |
| **[`HOME.md`](HOME.md)**                  | **Primary Navigation Hub** — Start here for daily navigation, topical index, capture links, and search tips.      |
| **[`CONTRIBUTING.md`](CONTRIBUTING.md)**  | **Taxonomy & Standards** — Frontmatter schema, naming conventions, note lifecycles, and security guidelines.      |
| **[`COMMIT.md`](COMMIT.md)**              | **Git & Push Guide** — Conventional commit conventions, pre-commit checklist, and push workflow.                  |
| **[`inbox/`](inbox/README.md)**           | **Zero-Friction Capture** — Drop untriaged thoughts, URLs, and quick snippets here (<30s mobile workflow).        |
| **[`templates/`](templates/README.md)**   | **Reusable Templates** — 10 standardized templates for concepts, troubleshooting, labs, procedures, and projects. |
| **[`procedures/`](procedures/README.md)** | **Actionable SOPs** — Step-by-step operational procedures, sync conflict resolution, and checklists.              |
| **[`knowledge/`](knowledge/README.md)**   | **Core Knowledge Library** — Topical documentation across cybersecurity, systems, education, and programming.     |

---

## 3. Repository Structure

```text
kbase/
├── README.md               # Repository documentation & architecture
├── HOME.md                 # Daily dashboard and entry point
├── CONTRIBUTING.md         # Note authoring standards, taxonomy, and rules
├── COMMIT.md               # Git commit conventions and push instructions
├── .editorconfig           # Editor consistency (UTF-8, LF, 2 spaces)
├── .gitattributes          # Git LF line-ending normalization
├── .gitignore              # Multi-OS, credential, and forensic-artifact exclusions
├── inbox/                  # Uncategorized capture zone (<30s notes)
├── knowledge/              # Reusable concepts and reference notes
│   ├── cybersecurity/      # DFIR, networking, web security, pentesting, research
│   ├── systems/            # Arch Linux, Windows 11, networking, virtualization
│   ├── education/          # Data structures, databases, academic & exam notes
│   ├── programming/        # Languages, algorithms, tooling, and architectures
│   ├── projects/           # High-level architecture & evergreen project concepts
│   ├── reference/          # Cheatsheets, syntax references, standards
│   └── personal/           # Personal workflows and development logs
├── procedures/             # Actionable, step-by-step repeatable workflows
│   ├── troubleshooting/    # Root cause analysis & fix procedures
│   ├── recovery/           # Disaster recovery & restoration guides
│   ├── checklists/         # Recurring review and verification lists
│   └── migration/          # Guidance for importing notes from Notion / Docusaurus
├── resources/              # Curated catalogs of external materials (books, articles, papers)
├── templates/              # Standardized Markdown templates
├── projects/               # Active project plans, milestones, and working logs
├── attachments/            # Diagrams and static assets (no sensitive data)
├── archive/                # Retired, superseded, or completed records
└── tools/                  # Lightweight, zero-dependency validation utilities
```

---

## 4. Security & OPSEC Warning

> [!WARNING]
> **Strict Secrets & Evidence Policy**
> This repository is synchronized via GitHub. Never commit:
> - Passwords, API tokens, access keys, or personal credentials.
> - SSH private keys (`id_rsa`, `id_ed25519`) or certificate private keys (`*.key`, `*.pem`).
> - Confidential client data, proprietary investigation evidence, or non-public breach data.
> - Raw packet captures (`*.pcap`), memory dumps (`*.raw`, `*.dmp`), disk images (`*.vmdk`), or event logs (`*.evtx`).
> 
> Always use sanitization placeholders (e.g., `<API_KEY>`, `example.com`, RFC 5737 IPs `192.0.2.1`).

---

## 5. Daily Authoring Workflow

### Rapid Mobile Capture (< 30 Seconds)
1. Open your mobile Markdown editor (e.g., Markor or Termux Vim on Android).
2. Create a new file in `inbox/` named with a short slug: `inbox/YYYY-MM-DD-topic.md`.
3. Jot down the thought, command, or URL using the [`templates/quick-capture.md`](templates/quick-capture.md) format.
4. Save and exit. The automated synchronization workflow will sync it across devices.

### Triage & Filing
During regular review (see [`procedures/checklists/weekly-inbox-review.md`](procedures/checklists/weekly-inbox-review.md)):
1. Move the note from `inbox/` to the relevant category under `knowledge/`, `procedures/`, or `projects/`.
2. Add standard YAML frontmatter (see [`CONTRIBUTING.md`](CONTRIBUTING.md)).
3. Update links and change the note status from `inbox` to `active` or `evergreen`.

---

## 6. Multi-Device Synchronization

Automated synchronization runs daily at 12:00 AM across configured environments:
- **Windows 11:** Windows Task Scheduler executing `C:\Users\Ankur\scripts\kbase-sync.sh` via Git Bash.
- **Arch Linux:** Automated or interactive Git pull/push workflow.
- **Android:** Termux cron / tasker synchronizing with the central GitHub remote.

For conflict resolution and rebase recovery instructions, consult [`procedures/synchronization-and-conflict-resolution.md`](procedures/synchronization-and-conflict-resolution.md).

---

## 7. Fast Search & Retrieval

Search your notes instantly from any terminal without external indexes:

```bash
# Search for a term across all notes (case-insensitive)
rg -i "btrfs snapshot"

# Search note titles / headings only
rg "^#+ .*DNS"

# Find notes by frontmatter type or topic
rg "^type: procedure"
rg "^  - dfir"
```

For complete searching instructions across CLI, GitHub UI, and mobile, see [`knowledge/reference/search-and-retrieval-guide.md`](knowledge/reference/search-and-retrieval-guide.md).