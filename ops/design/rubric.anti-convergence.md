# Design Anti-Convergence Rubric v1

Purpose: externalized judgment criteria for detecting distributional convergence
("AI slop") in generated UI. Consumed by `design-critic` (verdict) and
`design-director` (self-check before emitting a spec). This file is the single
source of truth; adapters must not duplicate its rules.

Scoring model: three tiers. T1 hits are mechanical and non-negotiable. T2 hits
are "default-not-choice" flags. T3 are judgment tests requiring reasoning.

---

## T1 — Hard tells (any hit → REVISE)

| ID | Pattern | Why it reads as AI |
|----|---------|--------------------|
| T1-01 | Display typography set in Inter / Roboto / Arial / system-ui without an explicit justification in DESIGN_SPEC | Statistical-median font of scraped web data |
| T1-02 | Purple/indigo gradient as primary accent (families around #6366F1, #7C3AED, #8B5CF6, #A855F7) | Dominant accent of 2022–2024 SaaS training data |
| T1-03 | Centered hero + 3–4 icon feature cards, when the content is not actually 3–4 parallel features | Highest-probability SaaS layout, applied regardless of content |
| T1-04 | ✨ sparkle glyphs or gradient text used to signify "AI" | Cliché signifier; carries zero information |
| T1-05 | Uniform border-radius plus low-opacity (~0.1) drop shadows applied globally | Framework-default styling, not a decision |
| T1-06 | Scroll fade-in on every section, or animation that encodes no information | Motion as decoration; flagged in YC design reviews as a vibe-coding tell |
| T1-07 | Hover states that reduce affordance (element fades/dims instead of gaining emphasis) | Violates basic affordance principles; common AI inversion |
| T1-08 | Numbered markers (01 / 02 / 03) on content that is not a genuine sequence | Structure as decoration; structure must encode truth about content |
| T1-09 | More than 3 distinct typographic roles inside the hero | Hierarchy noise; humans with typographic instincts do not arrive here |
| T1-10 | Any color or font-family not present in DESIGN_SPEC tokens (verify with `scripts/audit_tokens.py`) | Cross-section drift from multi-turn generation without shared context |

## T2 — Second-generation convergence (hit → REVISE unless the brief explicitly demands it)

These looks emerged as the new modes *after* first-generation anti-slop
guidance. They are legitimate designs, but they appear regardless of subject —
which makes them defaults, not choices. Treat them as evidence that the
distribution moved rather than dissolved.

| ID | Pattern |
|----|---------|
| T2-01 | Warm cream background (≈#F4F1EA family) + high-contrast serif display + terracotta/warm-clay accent (≈#D97757 — also Anthropic's Claude accent, doubly a tell) |
| T2-02 | Near-black background + a single acid-green or vermilion accent |
| T2-03 | Broadsheet look: hairline rules, zero border-radius, dense newspaper columns |

Disposition: if DESIGN_SPEC explicitly chose one of these *and* justified it
against the subject (T3-05), allow. Otherwise → REVISE with note
`default-not-choice`.

## T3 — Judgment tests (failure → REVISE with written rationale)

| ID | Test | How to run it |
|----|------|---------------|
| T3-01 | Substitution test | Replace the product name with a direct competitor's. If the design still "fits", it is not grounded in this subject. |
| T3-02 | Any-brief test | Would a generic one-line prompt in the same category ("modern SaaS landing page") plausibly produce this same plan? If yes, it is the distribution center. |
| T3-03 | Signature test | Name the single element this page will be remembered by. If you cannot name one, or there are three competing ones, fail. |
| T3-04 | Token-drift test | Do all sections derive from the same DESIGN_SPEC tokens (color, type, spacing convention)? Mechanical portion covered by T1-10; judge the rest visually. |
| T3-05 | Subject-grounding test | Point to at least two choices (palette, type, layout, motion, copy) that come from the subject's own world — its materials, instruments, vernacular. |
| T3-06 | Restraint test | Boldness is spent in exactly one place; everything around the signature is quiet and disciplined. Apply the Chanel rule: what one accessory should be removed? |

---

## Verdict contract

Emit exactly this block (machine-parseable by the orchestrator):

```
VERDICT: PASS | REVISE | ESCALATE
CONFIDENCE: HIGH | LOW        # LOW when no screenshot evidence was available
ITERATION: n/3
VIOLATIONS:
- [T1-02] src/components/Hero.tsx:41 — indigo gradient accent → replace with spec token A1 (#0E4F45)
- [T3-03] no identifiable signature element → propose one aligned with spec "Signature" section
```

Rules:
- REVISE must list violations with location + fix aligned to DESIGN_SPEC.
- ESCALATE when (a) iteration 3/3 is reached without PASS, or (b) the
  DESIGN_SPEC itself fails T3 — the spec is the defect, and re-direction is an
  outer-loop (human) decision, not an implementer retry.
- CONFIDENCE: LOW verdicts must state which evidence was missing.

## Known limitation (read before trusting yourself)

This rubric moves the output distribution; it does not eliminate convergence.
Whatever this rubric bans, a new mode will form around what remains. The only
durable anti-convergence input is a per-project design intent supplied by the
outer loop (subject, audience, brand constraints). When in doubt, ESCALATE to
the human rather than inventing taste.
