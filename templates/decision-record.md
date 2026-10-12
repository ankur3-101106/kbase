---
title: "ADR: <Decision Title>"
type: decision
area: projects
topics:
  - architecture
  - decision-record
status: active
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# ADR: <Decision Title>

## 1. Context & Problem Statement
Describe the architectural context, constraints, and the problem requiring a technical decision. What forces are driving this choice?

## 2. Decision Drivers
- Driver 1: e.g., Must work 100% offline on mobile and desktop.
- Driver 2: e.g., Must require zero runtime dependencies (no Node.js/Python for reading).
- Driver 3: e.g., Long-term format durability over 10+ years.

## 3. Considered Options
- **Option 1: <Option Name>** (e.g., Plain Markdown with Git synchronization)
- **Option 2: <Option Name>** (e.g., Self-hosted Obsidian Sync / CouchDB)
- **Option 3: <Option Name>** (e.g., Commercial Notion / Logseq sync)

## 4. Evaluation of Options

### Option 1: <Option Name>
- **Pros:** Full data ownership, zero cost, standard Git tooling, portable plain text.
- **Cons:** Occasional manual merge conflict resolution required when simultaneous offline edits occur.

### Option 2: <Option Name>
- **Pros:** Real-time synchronization.
- **Cons:** Server maintenance overhead, potential database lock-in.

## 5. Decision Outcome
- **Chosen Option:** Option 1 (<Option Name>)
- **Rationale:** Aligns best with core drivers of longevity, local-first operation, and cross-platform portability.

## 6. Consequences & Impact
- **Positive:** Notes remain readable anywhere; full version control history maintained in Git.
- **Negative:** Mobile capture requires basic Markdown discipline rather than rich graphical blocks.
- **Mitigation:** Provide `<30s` quick capture workflow to eliminate friction.
