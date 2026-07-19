# DESIGN_SPEC — <project / surface name>

Status: FROZEN | DRAFT
Author: design-director
Date: <yyyy-mm-dd>
Iteration: 1

This file is a contract. Implementers derive every visual value from it and may
not introduce colors, fonts, or motion outside it. Changing it is a
design-director action gated by the outer loop, never an implementer action.

---

## 1. Grounding

- Subject: <one concrete subject — what this product/page actually is>
- Audience: <who reads it, in one line>
- Single job: <the one thing this page must accomplish>
- ASSUMPTIONS: <anything pinned by the director because the brief was silent —
  outer loop should review these first>

## 2. Direction

<1–2 sentences stating the aesthetic point of view, and the ONE deliberate
risk this design takes and why the subject justifies it.>

Rejected alternatives (from divergence pass):
- Direction B: <one line> — rejected because <reason>
- Direction C: <one line> — rejected because <reason>

## 3. Tokens (machine-readable — audit_tokens.py parses this block)

<!-- TOKENS:BEGIN
colors: #000000, #FFFFFF
fonts: "Display Face", "Body Face", "Utility Face"
allow-extra: transparent, currentColor
TOKENS:END -->

Human-readable rationale:

| Token | Value | Role | Why (tie to subject) |
|-------|-------|------|----------------------|
| A1 | #...... | primary accent | ... |
| A2 | #...... | secondary accent | ... |
| N1 | #...... | background | ... |
| N2 | #...... | ink / foreground | ... |

| Face | Role | Why |
|------|------|-----|
| <display> | headlines, used with restraint | ... |
| <body> | reading text | ... |
| <utility> | captions / data (optional) | ... |

## 4. Layout

Concept (one sentence): <...>

```
+--------------------------------------+
|  ASCII wireframe of the key screen   |
+--------------------------------------+
```

## 5. Signature

The one element this page will be remembered by:
<name it, describe it, one paragraph max>

## 6. Motion policy

- Allowed: <specific, information-carrying moments — or "none">
- Forbidden: per rubric T1-06/T1-07 (blanket scroll fade-ins, affordance-reducing hovers)

## 7. Banned for this project

Inherited: all rubric T1 patterns. Project-specific additions:
- <e.g., no glassmorphism; no #D97757-family accents>

## 8. Quality floor (non-negotiable, do not announce in UI)

Responsive to mobile · visible keyboard focus · prefers-reduced-motion
respected · copy follows spec voice (plain verbs, sentence case, one job per
element).
