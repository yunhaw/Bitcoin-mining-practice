# Blockchain practice

###### Author:Raheem
###### Date: 2021.02.03
###### GitHub:

---

# Outline

1. Reference
1. 環境
1. 實作

## Reference

* 定義基本架構、功能與格式
https://lkm543.medium.com/%E7%94%A8python%E8%87%AA%E5%B9%B9%E4%B8%80%E5%80%8B%E5%8D%80%E5%A1%8A%E9%8F%88-1-10048ab8f095
* 利用非對稱加密簽署並發送交易
https://lkm543.medium.com/%E7%94%A8python%E8%87%AA%E5%B9%B9%E4%B8%80%E5%80%8B%E5%8D%80%E5%A1%8A%E9%8F%88-2-c581ddeed8ba
* 製作節點與用戶端程式
https://lkm543.medium.com/%E7%94%A8python%E8%87%AA%E5%B9%B9%E4%B8%80%E5%80%8B%E5%8D%80%E5%A1%8A%E9%8F%88-3-e455491bba72
* 節點間的廣播與同步
https://lkm543.medium.com/%E7%94%A8python%E8%87%AA%E5%B9%B9%E4%B8%80%E5%80%8B%E5%8D%80%E5%A1%8A%E9%8F%88-4-4c1b96081c79


## 環境

* IDE → Visual Studio Code
* Language → Python 3.8.5
* Module → hashlib, time

## 實作

### Hash

* 同樣的輸入值必會得到相同的輸出值
* 輸出的哈希數無法反推回原本的資料

### 非對稱加密 ( RSA )