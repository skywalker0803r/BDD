BDD研究
✅ 安裝與執行
bash
複製
編輯
# 建立虛擬環境（可選）
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 安裝依賴
pip install -r requirements.txt

# 執行 BDD 測試
make test-bdd

🧪 測試結果範例
yaml
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
