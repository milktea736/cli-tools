# 開關 OKD instances

## 運作方式
* 當使用者以 user client 進行 start / stop 時會註冊使用者工作狀態, 該狀態會以 JSON 型式被記錄到 S3 上, 當檔案被更改時會觸發 AWS Lambda
* AWS Lambda 會檢查當時: 
    * 任一使用者在工作狀態: 啟動 instances 
    * 所有使用者都不在工作狀態: 關閉 instances
* 本地端需要要有對應的 AWS credential, 並確認該帳號有權限操作記錄工作狀態 S3 上的 JSON 檔
* AWS Lambda 需要綁定 Role, 並建立 Policy 能開關相關的 instances 與讀取 S3 特定路徑的檔案

## user client
`working_status_manager.py` 進行使用者工作狀態的註冊.

## AWS Lambda
將 `okd_lambda.py` 放在 lambda, 並設定 S3 trigger.

