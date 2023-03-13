# CLI 小工具

- 大家可以利用小工具在註冊上下班狀態, 當有人需要使用時自動啟動 okd cluster, 大家都下班時關閉
- 將使用狀態更新到 S3 觸發 lambda, 在 lambda 中檢查開關機條件, 然後啟動或關閉相關機器

## Keywords

- Lambda
- S3
- EC2 / IAM