# DESIGN_SPEC — 「幾歲退休」RetireLab (retirement-age calculator, zh-TW)

Status: FROZEN
Author: design-director
Date: 2026-07-19
Iteration: 2

This file is a contract. Implementers derive every visual value from it and may
not introduce colors, fonts, or motion outside it. Changing it is a
design-director action gated by the outer loop, never an implementer action.

## Changelog

- 2026-07-23 (Iteration 2, gated amendment — Status stays FROZEN): Added
  dark-mode-only token **A2D `lamp-green-deep` #2E8168** for the P10 band edge.
  Fixes a confirmed contrast defect: the prior §3 note reused **A2 #0A3B30** as
  the dark-mode P10 edge, but A2 on SURFD `card-ink` #12201B measures ≈**1.35:1**
  — below the WCAG 3:1 graphics floor, i.e. the conservative lower-bound line is
  invisible on dark (screenshot-confirmed). A2 is a *light-mode-only* deep step;
  on a dark ground the pessimistic edge must be a **dimmer green than P50**, not a
  darker one. This amendment is scoped strictly to that one token decision; no
  other design value changed. Not an unfreeze — a gated correction.

---

## 1. Grounding

- Subject: A Traditional-Chinese (Taiwan) app that answers one question — 「你幾歲可以退休?」— by projecting a saver's money forward over time, honestly separating what is known (contributions to date) from what is uncertain (market outcomes: P90/P50/P10 for ETFs, a single deterministic line for individual stocks).
- Audience: Taiwanese retail investors planning retirement — people who have held a 郵局/銀行 存摺 (passbook) and a 勞保/勞退 對帳單 their whole adult life, and who are wary of being over-promised.
- Single job: On the result screen, let the user read their retirement age as a single confident figure while making the uncertainty behind it impossible to ignore — without lying with false precision.
- ASSUMPTIONS (outer loop review first):
  1. Delivery target is a native iOS/iPadOS + macOS app (README says 「App 內切換鈕」, dark mode via prop, Apple-heavy owner). This justifies a system zh-TW face (see T1-01 note). If the real target is a public web landing page, revisit the body-font decision.
  2. Full PRD is private; I pinned exact hex/type values. Brand may already own a locked green — I chose one adjacent to the prior-art #0F6E56 mark but did not copy it. Confirm against any brand book.
  3. TW market-color convention (紅漲綠跌) conflicts with green-as-growth branding. I resolved this by **never** using red/green to encode market direction (decision in §7). Confirm this is acceptable to the PRD.
  4. Chart series semantics: P50 = median (brand green), P90/P10 = one-hue band around it. Assumes the fan represents ONE quantity's distribution (correct per README), not categorical series.
  5. Two result archetypes share one signature (see §5): ETF = fork splits; individual-stock = fork stays a single line. Confirm the deterministic mode should visually *reuse* the same motif rather than get its own.

## 2. Direction

**存摺 (passbook ledger) as the governing artifact, with an honesty fork at "今天".** The screen behaves like a Taiwan bankbook: impact-printed tabular figures, thin ledger rules, cool passbook-paper stock, a running balance. Its one deliberate risk: the balance line is drawn *solid and printed* up to today, then — and only then — splits into the P90/P50/P10 fan. The seam between "printed past" and "fanned future" is the whole design. The subject justifies the risk because the product's核心倫理 is exactly this seam: 23-year sample, 權值股 concentration, 「P10–P90 非未來機率保證」. A calculator that hid the seam would be dishonest; this one makes it the hero.

Rejected alternatives (from divergence pass — axis = *governing metaphor*):
- Direction B — **時間地平線 (longevity horizon):** every screen hangs off one horizontal time-axis; the P50 retirement age is a horizon rule. Editorial, instrument-like, cool. Rejected because the horizon reads as generic data-viz — it survives the substitution test poorly (any robo-advisor could ship it) and it under-uses the deterministic-vs-probabilistic distinction that is this product's actual differentiator.
- Direction C — **財務健檢報告 (financial health-check report):** frame readiness like a Taiwanese 健檢報告 with risk bands and a readiness gauge. Rejected because a gauge compresses a *time* answer ("幾歲") into a dimensionless score, and "traffic-light gauge" invites the red/green market-color confusion (Assumption 3) plus the amber-caution semantics would collide with the readiness band.

Why A wins: the 存摺 is a distinctly Taiwanese financial artifact (fails a US competitor's substitution test), it grounds palette + type + copy + the signature all at once, and it turns the product's honesty requirement into its most memorable element instead of a footnote.

## 3. Tokens (machine-readable — audit_tokens.py parses this block)

<!-- TOKENS:BEGIN
colors: #0E5C48, #0A3B30, #6FB39B, #F1F4F0, #FFFFFF, #16211C, #D4DAD3, #B0741A, #F6ECD8, #B23A2E, #0C1512, #12201B, #E7EDE9, #3AA886, #26332D, #2E8168
fonts: "Space Mono", "PingFang TC", "Noto Sans TC"
allow-extra: transparent, currentColor
TOKENS:END -->

Human-readable rationale:

**Brand / neutral (light):**

| Token | Value | Role | Why (tie to subject) |
|-------|-------|------|----------------------|
| A1 `passbook-green` | #0E5C48 | primary accent · **P50 median** | The 存摺 cover / prior-art mark green, deliberately deepened; institutional, not a "market up" color. |
| A2 `ledger-green-deep` | #0A3B30 | **P10 lower bound (light only)** · deep type on green | Darkest step of the single-hue uncertainty band — the pessimistic edge reads as "more ink, less light." Light-mode only: on a dark ground it collapses below the contrast floor (see dark-band note + A2D). |
| C90 `band-green-light` | #6FB39B | **P90 upper bound** · fan tint | Lightest step of the same hue — optimistic edge; one hue = one honest quantity, never a second category. |
| N1 `passbook-paper` | #F1F4F0 | page background (light) | Cool green-grey passbook stock. Explicitly **not** cream (see §7 / T2-01). |
| SURF `card-paper` | #FFFFFF | raised card / ledger sheet | Clean printed sheet lifted off the paper page. |
| N2 `ledger-ink` | #16211C | foreground text | Near-black with a green cast — impact-printer ink, not pure #000. |
| N3 `rule-line` | #D4DAD3 | hairline ledger rules, borders, ticks | The thin printed rules of a passbook row grid. |

**Semantic (shared light/dark unless noted):**

| Token | Value | Role | Why |
|-------|-------|------|-----|
| WARN `stamp-amber` | #B0741A | risk揭露 · 行情過期條 · caution | The 官方戳章 amber of forms/stamps. Deliberately NOT #D97757 (§7). Used for the 個股 amber risk block and the stale-quote bar. |
| WARN-BG `amber-wash` | #F6ECD8 | fill behind amber bar / risk block | Low-chroma amber wash so the caption stays legible. |
| ERR `error-brick` | #B23A2E | error state only | A muted brick red reserved strictly for the 錯誤 state variant — never for market direction. |

**Dark mode:**

| Token | Value | Role | Why |
|-------|-------|------|-----|
| N1D `ink-bg` | #0C1512 | page background (dark) | Deep ledger-ink ground; the passbook read under lamplight. |
| SURFD `card-ink` | #12201B | raised card (dark) | Barely-lifted surface, keeps flat ledger feel. |
| N2D `paper-fg` | #E7EDE9 | foreground text (dark) | Warm paper-white ink on dark. |
| A1D `green-lamp` | #3AA886 | primary accent · P50 (dark) | Brightened passbook green for AA on dark — muted, never acid (§7 / T2-02). |
| A2D `lamp-green-deep` | #2E8168 | **P10 lower bound (dark only)** · pessimistic band edge | The dimmed passbook lamp: same hue as A1D (≈162°), same saturation family, but ~1.8× less luminous — so it reads as the conservative "more ink, less light" edge, not a second accent. On dark, the pessimistic step must be a *dimmer* green than P50, not a darker one (a darker green vanishes into the ground). Clears the 3:1 graphics floor on both dark grounds: **3.57:1** on SURFD #12201B, **3.94:1** on N1D #0C1512. |
| N3D `rule-dark` | #26332D | hairline rules (dark) | Ledger rules on dark. |

Dark-mode band: P90 = A1D lightened via opacity on SURFD; **P10 = A2D `lamp-green-deep` #2E8168** — a dimmed same-hue green that reads as the pessimistic "more ink, less light" edge while clearing the 3:1 graphics floor on both dark grounds (3.57:1 on SURFD, 3.94:1 on N1D). A2 #0A3B30 is the light-mode-only deep step and **must not** be reused on dark: there it measures ≈1.35:1 on SURFD and the conservative lower-bound line disappears. WARN/WARN-BG/ERR carry across both modes (amber/red keep meaning in either).

**Type:**

| Face | Role | Why |
|------|------|-----|
| **Space Mono** | display **figures only** — the hero age「XX 歲」, 餘額 amounts, chart tick/P-value readouts | Impact-printed, tabular, slightly mechanical — the dot-matrix voice of a passbook line-printer. Latin/digits only; carries the characterful load, used with strict restraint (never for prose). |
| **PingFang TC** (fallback: **Noto Sans TC**, sans-serif) | body — all zh-TW reading text, headings, labels | System zh-TW face on the target platform. **T1-01 justification:** native iOS/macOS rendering gives the best Traditional-Chinese hinting/vertical-metrics at small sizes on-device; shipping a webfont zh-TW here would trade render quality for no brand gain, since the characterful voice lives in the figures. Noto Sans TC is the non-Apple fallback so the app degrades honestly off-platform. |

Spacing / convention (for T3-04 coherence): 4px base grid; ledger row height 44px (min tap target); rules are 1px `rule-line`; card radius 12px (soft-printed corner, one value everywhere); figures always right-aligned with tabular numerals.

## 4. Layout

Concept (one sentence): A single-column passbook page — a running ledger of what you put in (printed, known) resolving into the answer figure and one balance line that forks from solid into fan at 「今天」.

```
+----------------------------------------------+
|  幾歲退休            [ETF 型]  [·過期 amber?] |  <- top bar; stale-quote bar sits here
+----------------------------------------------+
|                                              |
|  你可以在                                    |  <- zh label (PingFang TC)
|      58 歲  退休                             |  <- HERO figure (Space Mono, huge)
|  以 P50 中位數估算 · 機率語句                 |  <- caption
|                                              |
+----------------------------------------------+
|  結餘 / 投入明細  (ledger rows, hairline)    |
|  ----------------------------------------    |
|  月投入        NT$ 15,000                     |  <- tabular figs, right-aligned
|  年報酬(SWR)   4.0%                          |
|  ----------------------------------------    |
|                                              |
|   THE FORK  (signature §5)                   |
|                     ______  P90 6FB39B       |
|   printed solid    /                         |
|   ============@===<====== P50 0E5C48 (A1)    |  <- @ = 「今天」stamp/tick
|   (known past)     \______ P10 0A3B30 (A2)   |
|            today ->|<- uncertain future      |
|                                              |
|  [ 簡單 P90/P50/P10 三卡  |  進階 fan chart ] |  <- mode toggle
|  +--------+ +--------+ +--------+             |
|  |  P90   | |  P50   | |  P10   |             |  <- three cards echo band hues
|  | 54 歲  | | 58 歲  | | 65 歲  |             |
|  +--------+ +--------+ +--------+             |
|                                              |
|  資料來源:23 年樣本 · 權值股集中 ·           |  <- caveat, always present
|  P10–P90 非未來機率保證                       |
+----------------------------------------------+
```

Note: the ASCII fork above depicts the **light-mode** fork (P10 = A2 #0A3B30 on paper). In dark mode the P10 stroke uses **A2D #2E8168** (see §3 dark-band note); everything else in the layout is mode-agnostic.

Individual-stock variant: identical shell, but the balance line stays a **single printed line** past 「今天」 (no fork), a 「確定性試算」stamp sits at the top-right instead of 「ETF 型」, and the P90/P50/P10 cards are replaced by one figure + the amber risk block (WARN / WARN-BG). The absence of the fork is the honest signal: no probability, so no band.

## 5. Signature

**「存摺分岔線」— the Passbook Fork.** One horizontal balance line is drawn impact-printed and solid from the start of saving up to a stamped 「今天」 tick; at that exact tick it either splits into the P90/P50/P10 fan (ETF, single-hue green band) or continues as one unbroken line (individual stock, deterministic). The seam is the only place emphasis is spent: the past is flat and printed; the future either fans or does not. This one element states the product's entire ethic — known vs. unknown — and reappears shrunk to a glyph as the app motif. It is nameable, singular, and does double duty as the difference between the two result archetypes.

## 6. Motion policy

- Allowed: on result reveal, the balance line **prints left-to-right once** (like a passbook line-printer advancing), and the fan opens only *after* the 「今天」 tick is reached — motion that encodes the known→uncertain sequence. Mode toggle (簡單/進階) cross-fades the chart region only. Slider in 進階 mode updates the fan live (direct manipulation, information-carrying).
- Forbidden: per rubric T1-06/T1-07 — no blanket scroll fade-ins, no decorative section reveals, no hover states that dim/fade an element instead of adding emphasis. `prefers-reduced-motion` → line and fan render instantly, no print sweep.

## 7. Banned for this project

Inherited: all rubric T1 patterns. Project-specific additions:
- No terracotta / warm-clay accents (#D97757 family) and no cream page (#F4F1EA family) — the paper is cool green-grey #F1F4F0. Steers clear of T2-01.
- No serif display face. The characterful voice is the mono *figure*, not a serif headline (also T2-01).
- No acid-green / vermilion-on-near-black dark mode — dark accent is muted passbook green #3AA886. Steers clear of T2-02.
- No dense multi-column broadsheet layout. Ledger hairlines here are the 存摺 artifact (T3-05), single-column and app-native, not newspaper columns. Distinguishes from T2-03.
- **No red/green to encode market up/down.** TW convention (紅漲綠跌) conflicts with green-as-brand; the uncertainty band is single-hue green (P90→P50→P10), red is reserved for the error state only, amber for caution only.
- No probability language, percentages, or fan band on the individual-stock screen — deterministic 「確定性試算」only (product rule; violating it is a correctness bug, not a style choice).
- No purple/indigo gradients, no glassmorphism, no global uniform-radius + soft-shadow framework default.

## 8. Quality floor (non-negotiable, do not announce in UI)

Responsive to mobile · visible keyboard focus · prefers-reduced-motion
respected · copy follows spec voice (plain verbs, sentence case, one job per
element) · all figures use tabular numerals and consistent NT$ formatting ·
AA contrast in both light and dark token sets.
</content>
</invoke>
