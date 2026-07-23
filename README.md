# retirelab-design — 「幾歲退休」設計稿 Demo

Live Demo:https://gary-gaga.github.io/retirelab-design/
需求正本:私有 repo `retirelab` 之 `docs/PRD.md`(本 repo 只放 Claude Design 匯出物,不放文件)。

## 版本對照(防漂移記帳)

| 匯出日期 | 檔案 | 對應 PRD 版本 | 涵蓋畫面 / 備註 |
|---|---|---|---|
| 2026-07-23 | index.html(critique 32/40 全清單修復) | PRD v0.8 ⑧ | Impeccable dual-agent critique(快照 `.impeccable/critique/`)後五階段修復:①誠信+文案 — 個股/無法達標頁補合成資料標示、設定頁「隨時可改」承諾落地(試算參數列可點回缺口引導)、加入帳本/賣超改白話就地錯誤、hero caption 修破碎中文、F-xx 內部代號清出使用者文案;②目標頁「希望幾歲前退休」滑桿(50–75 預設 60)— fail 判定改用自選年齡、無法達標提醒兩種模式就地出現、個股報酬 2–10% 可調(接引擎 solveMonths);③a11y+效能 — aria-live 結果播報、tabbar 改 nav 語意、P90 標籤對比 AA、觸控目標 44px、MC memoize+離屏延算(拖曳 60–100×);④polish — .link 全域樣式、mono 僅限數字、提領期強調改回 P50、標題層級;⑤終審修復 — s-fail 直開改示範狀態(不再「仍差 0 萬」)、個股頁就地提醒(無機率語句,連往調整計畫)。黃金值 58 歲/1,500 萬不變;navtest 50 項 ALL-PASS |
| 2026-07-20 | index.html(新手友善精簡) | PRD v0.8 ⑥ | 漸進揭露(不刪功能、預設值不變):缺口引導一題版(只問月支出;勞保/勞退/SWR 收摺疊)、投入頁「更多選項」摺疊(調升/資產來源)、帳本三摺疊(報酬對照與配息/新增持股/自動配息)、白話註 4 處、`details.fold` 元件(零新色彩)。黃金值 58 歲/1,500 萬不變;navtest 34 項 ALL-PASS |
| 2026-07-20 | index.html + engine.js(再審視修復) | PRD v0.8 | 雙鏡片第二輪修復:①追蹤頁接真 — 進度=帳本市值(與帳本同源,殺掉最後假畫面),投入列表/累積投入由交易紀錄推導;②配置圖顏色改跟隨標的(metadata 固定,dataviz「color follows entity」);③比較/提領期接入 App 流程(結果頁連結+返回鍵);④tour 更新為 12 步(含比較/持股明細);⑤提領期自實際 P50 達標年齡起算;⑥每年調升滑桿接真(engine annualContributionGrowth,預設 0% 保 58 歲 signature,拉 10% 可見提早 6 年);⑦新增持股與加碼統一計費口徑。navtest 32 項 ALL-PASS |
| 2026-07-21 | index.html(內容盲區修復+目標雙模式) | PRD v0.8 ⑦ | ①免責頁改版:價值主張先行、P10–P90 行話改白話、合成資料標示、方法連結;②標的頁/三卡/SWR 去行話;③目標頁 User Story 開場+雙模式:「以每月現金流推算」(F-09)/「直接設定金額」(F-01 可覆寫,1,000 萬–2 億,不限退休語境),全下游含無法達標三條路(direct 模式路三=目標調降 150 萬)照切換後目標計算;手機導覽改換行 chip。navtest 37 項 ALL-PASS |
| 2026-07-20 | index.html(帳本精簡+持股明細) | PRD v0.8 F-12 | 共 17 畫面。帳本改版:持股列表 → 市值占比橫條圖(單色綠明度階固定順序,dataviz 驗證 CVD ΔE 28.9 PASS;低彩度以列表籤補救)+ 可點配置列;新增第 17 畫面「持股明細」:單檔市值/均價/未實現/已實現/年配息 + 調整區(改現價/加碼/減碼,賣超由引擎驗證擋下)+ 本檔交易紀錄;帳本頁移除全域交易列表(移入明細)。navtest 27 項 ALL-PASS |
| 2026-07-20 | index.html(持股輸入→試算起點) | PRD v0.8 F-12×F-01 | 帳本頁新增「新增持股」表單(標的 chips 由 fixtures metadata 動態生成含 00940 短史警示,Rule 2;股數/含費用成本/手動現價);投入頁「已累積資產」可切換手動示範值/帳本市值(portfolioValue),切換後全下游試算連動。navtest 增 2 項斷言(共 24 項) |
| 2026-07-20 | index.html + engine.js(Demo 完整化) | PRD v0.8 | 共 16 畫面。①MVP 補完:缺口引導三滑桿接 `gap.ts`(目標動態化,全下游連動)、稅費接 `tax.ts`(級距 chips/含不含切換真算,feeNote 動態:12% 級距實測差 +0.4 年)、新增「方法揭露」頁;②v1.1 前移:「標的比較」頁(0050 vs 0056 雙 MC,P50 差 2.4 年)、帳本「配息自動生成」示意(mock 除息事件 × 真持股);③v2.0 概念驗證:「提領期」頁接 engine `decumulation`(§6.8);④`?tour=1` 自導覽(10 步三幕腳本)。navtest 增 7 項斷言 |
| 2026-07-20 | index.html(帳本畫面組出稿) | PRD v0.7 F-12 / §6.7 | 新增第 11 畫面「帳本」+ tabbar 第 4 tab:持有市值 hero、持股卡(均價/未實現損益)、三數字誠實對照(簡單法/XIRR/計畫假設,口徑標示)、已實現損益、年度配息(總額+最大標的)、最近交易(含手續費/證交稅)。全部數字由 engine ledger/xirr 模組計算(合成交易 9 筆、現價手動輸入,Rule 3/7);文案沿用 copy-registry ledger.* 條目;損益以 +/− 中性呈現(禁紅綠漲跌)。共 13 畫面 |
| 2026-07-20 | index.html + engine.js(真引擎接線) | PRD v0.7 | demo 數字全面改為 `@retirelab/engine` 真實輸出:`engine.js`(9.5KB IIFE,主 repo `npm run bundle:demo-engine` 產生,內含 fixtures 合成資料)驅動 ETF 結果(MC 1,000 次、seed 42、實質報酬=名目÷通膨 2%)、個股封閉解、無法達標頁(門檻:60 歲前退休);示範情境改為目標 1,500 萬/缺口 50,000(原 375 萬在合成報酬下全情境過早達標,故事撐不起來);投入/年齡/進階 slider 雙向同步且驅動真模擬;結果頁 caption 標示合成資料+通膨假設;追蹤頁進度改 1,400,000(修正報酬=0 的不自洽);無引擎時 fallback 舊估算式。每年調升 slider 仍為純視覺(engine 未支援投入遞增)。navtest ALL-PASS、audit_tokens 歸零 |
| 2026-07-20 | index.html(就地 patch) | PRD v0.7 F-01 | 「投入」畫面之目前年齡由靜態文字改為 slider(18–80,預設 35);結果 ETF 頁 hero 與 P90/P50/P10 三卡年齡依年齡差量位移(demo 假邏輯,非引擎輸出)。`audit_tokens.py` 歸零 |
| 2026-07-19 | index.html | v0.2 規格 + DESIGN_SPEC(FROZEN) | 12 畫面依 `design/DESIGN_SPEC.md`「存摺分岔線」重新實作:存摺帳頁語彙(等寬印字數字、細帳簿線、冷綠灰紙色 #F1F4F0)、結果頁餘額線於「今天」分岔(ETF=P90/P50/P10 單色綠扇形;個股=單線+確定性試算戳章,無機率語句)、light/dark tokens、print 動效 + prefers-reduced-motion、`?s=N&theme=dark&mode=adv` deep link;瀏覽/App 雙模式(`?app=1` 或右上切換,App 模式可實際操作完整流程:onboarding→結果、底部 tab、低投入→調整建議)。`audit_tokens.py` 歸零 + design-critic 驗收;`ops/design/tests/navtest.html` 為導航回歸測試(headless Chrome dump-dom 執行) |
| 2026-07(初版) | archive/v0.1.html | v0.2 規格 + design review G1–G8 | 12 畫面(載入/免責/缺口引導/目標/投入/標的/結果 ETF+個股雙型/無法達標/追蹤/設定/狀態變體);G1–G8 已納入:缺口引導(Onboarding 1/4,勞動部外連、SWR 3–5% 預設 4%)、稅費設定(級距 5/12/20/30/40 預設 12%、手續費預設 6 折、含/不含切換附年數差)、個股結果頁(確定性試算徽章、單線圖、amber 風險揭露、無機率語句)、ETF 簡單/進階雙模式(簡單=機率語句+P90/P50/P10 三卡;進階=fan chart+滑桿「快速估算/模擬結果」;首次 30 秒引導可跳過)、四態變體(skeleton/空/錯誤/行情過期 amber 條)、資料來源補充(23 年樣本、權值股集中、P10–P90 非未來機率保證)。dark mode tokens 已備(App 內切換鈕未做,由 prop 控制) |

## 更新流程

Claude Design 匯出 standalone HTML → 舊 `index.html` 移入 `archive/vX.Y.html` → 新檔覆蓋 `index.html` → 上表加一列 → push(Pages 自動更新)。
