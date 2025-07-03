Feature: 投手姿勢分析

  Scenario: 教練上傳影片後取得 landing frame
    Given 教練已準備好一段投球影片
    When 教練上傳該影片至系統
    Then 系統應回傳 landing frame 資訊
