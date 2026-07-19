---
name: design-direction
description: Anti-convergence workflow for any UI/frontend visual work. Use this skill whenever a task creates a new UI surface, restyles an existing one, builds a landing page, dashboard, component library, or when the user says a design "looks AI-generated", "generic", "沒有記憶點", or asks to "make it look better". Also use before ANY frontend implementation task that has no DESIGN_SPEC.md yet — implementation must not start without one.
---

# Design Direction (harness adapter)

Core files (single source of truth — read, never duplicate):

- Rubric: `ops/design/rubric.anti-convergence.md`
- Spec contract template: `ops/design/template.design-spec.md`
- Mechanical audit: `ops/design/scripts/audit_tokens.py`

## Hard rules

1. No UI implementation before a FROZEN `design/DESIGN_SPEC.md` exists.
2. The spec is a contract: every color/font/motion value derives from its
   tokens. Implementers never edit the spec; spec changes route through
   `design-director` and are outer-loop gated.
3. "Done" for any visual task requires a `design-critic` verdict of PASS.
4. Run `python ops/design/scripts/audit_tokens.py --spec design/DESIGN_SPEC.md
   --src <src>` after implementation edits; treat any exit ≠ 0 as a failing
   test.

## Routing

| Situation | Action |
|-----------|--------|
| New surface, or no DESIGN_SPEC.md | Dispatch `design-director` first. Do not sketch UI yourself. |
| Change within an existing FROZEN spec | Implement directly from tokens, then run audit + dispatch `design-critic`. |
| Vague aesthetic ask ("make it better", "太 AI 了") | This is a re-direction request → `design-director`, not ad-hoc tweaks. |
| Critic returns REVISE | Implementer fixes listed violations only; re-run critic. Max 3 iterations. |
| Critic returns ESCALATE | Stop. Surface the verdict to the human (outer loop). |

## Why this exists (context for the model)

LLM UI output converges to the statistical center of training data
("distributional convergence" → the "AI slop" aesthetic). Rubrics only move
the distribution; the durable fix is per-project design intent captured in a
frozen spec, plus a critic gate with mechanical token auditing. Your job is to
follow the pipeline, not to trust your own defaults.
