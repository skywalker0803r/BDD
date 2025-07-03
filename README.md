# 🎯 BDD 投手姿勢分析測試專案

本專案示範如何使用 **Behavior-Driven Development (BDD)** 方法，針對棒球投手影片分析服務進行測試。使用框架為 `FastAPI + Behave`。

---

## ✅ 安裝與執行

```bash
# 建立虛擬環境（可選）
python -m venv .venv
# Windows 系統
.venv\Scripts\activate
# macOS/Linux 系統
source .venv/bin/activate

# 安裝依賴套件
pip install -r requirements.txt

# 執行 BDD 測試
behave features/
💡 Windows 系統無法使用 make 指令，請改用 behave features/。

📁 專案結構
bash
複製
編輯
.
├── app/
│   └── main.py                 # FastAPI 主程式
├── features/
│   ├── pitch_analysis.feature  # Gherkin 規格
│   └── steps/
│       └── pitch_steps.py      # Behave 測試步驟
├── requirements.txt
└── README.md
🧪 測試結果範例
text
複製
編輯
Feature: 投手姿勢分析      # features/pitch_analysis.feature:1

  Scenario: 教練上傳影片後取得 landing frame
    Given 教練已準備好一段投球影片
    When 教練上傳該影片至系統
    Then 系統應回傳 landing frame 資訊

1 feature passed, 0 failed
1 scenario passed, 0 failed
3 steps passed, 0 failed
📦 相關技術與工具
FastAPI

Behave

Gherkin 語法介紹

📌 目標
實作一個投手姿勢影片分析 API，並使用 BDD 驗證以下場景：

教練上傳影片

系統完成姿勢分析

回傳 landing frame 結果供前端儀表板使用

🗂️ 待辦
 實作真實的姿勢偵測模型分析

 整合 CI/CD 自動跑 BDD 測試

 製作測試報告輸出 HTML 格式

python
複製
編輯

這份 README.md 支援 GitHub 顯示，格式清晰並且說明完整。如你想進一步加上範例圖、badge、CI 腳本等也可
