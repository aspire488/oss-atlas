# Engineering Learnings

<sub>THE RECORD / 04</sub>

Reusable engineering principles extracted from actual open-source work. These are patterns supported by contribution evidence, not generic advice or proficiency claims.

---

## Current principles

| Principle | Why it matters |
|:--|:--|
| Preserve semantic signals across streaming boundaries. | A transport boundary must not erase meaningful completion or error state. |
| Treat NULL, empty, and sentinel values as distinct domain identities. | Collapsing them can change query and application behavior. |
| Protect aggregate queries from join multiplication. | Correct-looking rows can still produce incorrect totals. |
| Prefer evidence-backed metrics over activity proxies. | A count is not a measure of impact. |
| Separate upstream acceptance from fork-side implementation. | Prepared work is not an upstream contribution. |
| Treat maintainer feedback as engineering input. | Review often exposes compatibility and scope constraints. |
| Record verification scope precisely. | A focused test does not prove the full system works. |

## Standard for a new learning

Every entry must link to at least one upstream artifact or case study and include:

- the observed engineering problem
- the constraint or failure mode
- the reusable principle
- supporting evidence
- limits or counterexamples, where known

---

<sub>Good learnings compress experience without removing the evidence that made them true.</sub>
