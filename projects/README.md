# Active & Tracked Projects (`projects/`)

Planning documents, Architecture Decision Records (ADRs), milestones, and working logs for personal, academic, and open-source projects.

---

## 📂 Layout Convention
Each major project has its own dedicated folder under `projects/`:

```text
projects/
├── README.md
└── <project-slug>/
    ├── README.md             # Project overview (from templates/project-overview.md)
    ├── decisions/            # Architecture decision records (from templates/decision-record.md)
    └── logs/                 # Working session logs and retrospectives
```

---

## 🚀 Lifecycle of a Project
1. **Planning & Kickoff:** Create project directory and initialize `README.md`.
2. **Active Development:** Track ongoing milestones and link relevant code repositories.
3. **Completion / Retirement:** Once completed or decommissioned, move the project directory to `archive/<YYYY>-<project-slug>/`.
