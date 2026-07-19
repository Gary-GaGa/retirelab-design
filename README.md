# retirelab-design — 「幾歲退休」設計稿 Demo

Live Demo:https://gary-gaga.github.io/retirelab-design/
需求正本:私有 repo `retirelab` 之 `docs/PRD.md`(本 repo 只放 Claude Design 匯出物,不放文件)。

## 版本對照(防漂移記帳)

| 匯出日期 | 檔案 | 對應 PRD 版本 | 涵蓋畫面 / 備註 |
|---|---|---|---|
| 2026-07-19 | index.html | v0.2 規格 + DESIGN_SPEC(FROZEN) | 12 畫面依 `design/DESIGN_SPEC.md`「存摺分岔線」重新實作:存摺帳頁語彙(等寬印字數字、細帳簿線、冷綠灰紙色 #F1F4F0)、結果頁餘額線於「今天」分岔(ETF=P90/P50/P10 單色綠扇形;個股=單線+確定性試算戳章,無機率語句)、light/dark tokens、print 動效 + prefers-reduced-motion、`?s=N&theme=dark&mode=adv` deep link;瀏覽/App 雙模式(`?app=1` 或右上切換,App 模式可實際操作完整流程:onboarding→結果、底部 tab、低投入→調整建議)。`audit_tokens.py` 歸零 + design-critic 驗收;`ops/design/tests/navtest.html` 為導航回歸測試(headless Chrome dump-dom 執行) |
| 2026-07(初版) | archive/v0.1.html | v0.2 規格 + design review G1–G8 | 12 畫面(載入/免責/缺口引導/目標/投入/標的/結果 ETF+個股雙型/無法達標/追蹤/設定/狀態變體);G1–G8 已納入:缺口引導(Onboarding 1/4,勞動部外連、SWR 3–5% 預設 4%)、稅費設定(級距 5/12/20/30/40 預設 12%、手續費預設 6 折、含/不含切換附年數差)、個股結果頁(確定性試算徽章、單線圖、amber 風險揭露、無機率語句)、ETF 簡單/進階雙模式(簡單=機率語句+P90/P50/P10 三卡;進階=fan chart+滑桿「快速估算/模擬結果」;首次 30 秒引導可跳過)、四態變體(skeleton/空/錯誤/行情過期 amber 條)、資料來源補充(23 年樣本、權值股集中、P10–P90 非未來機率保證)。dark mode tokens 已備(App 內切換鈕未做,由 prop 控制) |

## 更新流程

Claude Design 匯出 standalone HTML → 舊 `index.html` 移入 `archive/vX.Y.html` → 新檔覆蓋 `index.html` → 上表加一列 → push(Pages 自動更新)。
