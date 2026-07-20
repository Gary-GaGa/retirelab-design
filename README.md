# retirelab-design — 「幾歲退休」設計稿 Demo

Live Demo:https://gary-gaga.github.io/retirelab-design/
需求正本:私有 repo `retirelab` 之 `docs/PRD.md`(本 repo 只放 Claude Design 匯出物,不放文件)。

## 版本對照(防漂移記帳)

| 匯出日期 | 檔案 | 對應 PRD 版本 | 涵蓋畫面 / 備註 |
|---|---|---|---|
| 2026-07-20 | index.html(持股輸入→試算起點) | PRD v0.8 F-12×F-01 | 帳本頁新增「新增持股」表單(標的 chips 由 fixtures metadata 動態生成含 00940 短史警示,Rule 2;股數/含費用成本/手動現價);投入頁「已累積資產」可切換手動示範值/帳本市值(portfolioValue),切換後全下游試算連動。navtest 增 2 項斷言(共 24 項) |
| 2026-07-20 | index.html + engine.js(Demo 完整化) | PRD v0.8 | 共 16 畫面。①MVP 補完:缺口引導三滑桿接 `gap.ts`(目標動態化,全下游連動)、稅費接 `tax.ts`(級距 chips/含不含切換真算,feeNote 動態:12% 級距實測差 +0.4 年)、新增「方法揭露」頁;②v1.1 前移:「標的比較」頁(0050 vs 0056 雙 MC,P50 差 2.4 年)、帳本「配息自動生成」示意(mock 除息事件 × 真持股);③v2.0 概念驗證:「提領期」頁接 engine `decumulation`(§6.8);④`?tour=1` 自導覽(10 步三幕腳本)。navtest 增 7 項斷言 |
| 2026-07-20 | index.html(帳本畫面組出稿) | PRD v0.7 F-12 / §6.7 | 新增第 11 畫面「帳本」+ tabbar 第 4 tab:持有市值 hero、持股卡(均價/未實現損益)、三數字誠實對照(簡單法/XIRR/計畫假設,口徑標示)、已實現損益、年度配息(總額+最大標的)、最近交易(含手續費/證交稅)。全部數字由 engine ledger/xirr 模組計算(合成交易 9 筆、現價手動輸入,Rule 3/7);文案沿用 copy-registry ledger.* 條目;損益以 +/− 中性呈現(禁紅綠漲跌)。共 13 畫面 |
| 2026-07-20 | index.html + engine.js(真引擎接線) | PRD v0.7 | demo 數字全面改為 `@retirelab/engine` 真實輸出:`engine.js`(9.5KB IIFE,主 repo `npm run bundle:demo-engine` 產生,內含 fixtures 合成資料)驅動 ETF 結果(MC 1,000 次、seed 42、實質報酬=名目÷通膨 2%)、個股封閉解、無法達標頁(門檻:60 歲前退休);示範情境改為目標 1,500 萬/缺口 50,000(原 375 萬在合成報酬下全情境過早達標,故事撐不起來);投入/年齡/進階 slider 雙向同步且驅動真模擬;結果頁 caption 標示合成資料+通膨假設;追蹤頁進度改 1,400,000(修正報酬=0 的不自洽);無引擎時 fallback 舊估算式。每年調升 slider 仍為純視覺(engine 未支援投入遞增)。navtest ALL-PASS、audit_tokens 歸零 |
| 2026-07-20 | index.html(就地 patch) | PRD v0.7 F-01 | 「投入」畫面之目前年齡由靜態文字改為 slider(18–80,預設 35);結果 ETF 頁 hero 與 P90/P50/P10 三卡年齡依年齡差量位移(demo 假邏輯,非引擎輸出)。`audit_tokens.py` 歸零 |
| 2026-07-19 | index.html | v0.2 規格 + DESIGN_SPEC(FROZEN) | 12 畫面依 `design/DESIGN_SPEC.md`「存摺分岔線」重新實作:存摺帳頁語彙(等寬印字數字、細帳簿線、冷綠灰紙色 #F1F4F0)、結果頁餘額線於「今天」分岔(ETF=P90/P50/P10 單色綠扇形;個股=單線+確定性試算戳章,無機率語句)、light/dark tokens、print 動效 + prefers-reduced-motion、`?s=N&theme=dark&mode=adv` deep link;瀏覽/App 雙模式(`?app=1` 或右上切換,App 模式可實際操作完整流程:onboarding→結果、底部 tab、低投入→調整建議)。`audit_tokens.py` 歸零 + design-critic 驗收;`ops/design/tests/navtest.html` 為導航回歸測試(headless Chrome dump-dom 執行) |
| 2026-07(初版) | archive/v0.1.html | v0.2 規格 + design review G1–G8 | 12 畫面(載入/免責/缺口引導/目標/投入/標的/結果 ETF+個股雙型/無法達標/追蹤/設定/狀態變體);G1–G8 已納入:缺口引導(Onboarding 1/4,勞動部外連、SWR 3–5% 預設 4%)、稅費設定(級距 5/12/20/30/40 預設 12%、手續費預設 6 折、含/不含切換附年數差)、個股結果頁(確定性試算徽章、單線圖、amber 風險揭露、無機率語句)、ETF 簡單/進階雙模式(簡單=機率語句+P90/P50/P10 三卡;進階=fan chart+滑桿「快速估算/模擬結果」;首次 30 秒引導可跳過)、四態變體(skeleton/空/錯誤/行情過期 amber 條)、資料來源補充(23 年樣本、權值股集中、P10–P90 非未來機率保證)。dark mode tokens 已備(App 內切換鈕未做,由 prop 控制) |

## 更新流程

Claude Design 匯出 standalone HTML → 舊 `index.html` 移入 `archive/vX.Y.html` → 新檔覆蓋 `index.html` → 上表加一列 → push(Pages 自動更新)。
