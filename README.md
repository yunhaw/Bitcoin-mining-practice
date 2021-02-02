# Bitcoin mining practice

###### Author: Raheem
###### Date: 2021.01.30
###### Source: https://hackmd.io/@Raheem/ByJHtQVxd

---

# Outline

1. Reference
2. 環境
3. 實作

## Reference

* Tutorial → https://www.youtube.com/watch?v=ZhnJ1bkIWWk&list=LL&index=1
* Source code → https://github.com/codebasics/cool_python_apps/blob/main/2_bitcoin_mining/bitcoin_mining.py

## 環境

* IDE → Visual Studio Code
* Language → Python 3.8.5
* Module → hashlib, time

## 實作

### 挖礦

* 區塊屬性 = ( 區塊編號, 交易內容, 前一塊的雜湊值, 猜測值 )

    | `區塊屬性`     |
    |:------------- |
    | block_number  |
    | transactions  |
    | previous_hash |
    | Nonce         |

* 雜湊值 ( Hash ) = block_number + transactions + previous_hash + Nonce
    ###### example：
    
    | `區塊屬性`     | `內容`                                         | 
    | ------------- | ---------------------------------------------- |
    | block_number  | 2                                              | 
    | transactions  | Raheem -> dog -> 20<p/>dog -> cat -> 45        |
    | previous_hash | 3db3bdbd49052dd9c713e02f91c1e1bda1704b7732024a49d98277b632300cd9 |
    | Nonce         | 7417                                           |

    經過 SHA256 →
    Hash = 000031a57e9c7479cd6bf6f77c953b843eafad24b36cbded64c5c3af0970d658

* 挖礦難度 ( Difficulty ) = 設定挖礦難度，代表生成的Hash值開頭有幾個 0 ( 題目 )

* 猜測值 ( Nonce ) = 加上此值可使得Hash值滿足挖礦設定的難度 ( 解答 )
    
* 產生新區塊的條件 ( 挖礦成功 )：
    ###### example：
        Difficulty = 4
        表示區塊內容加入Nonce後，Hash值的開頭必須滿足 4 個零
        當 Nonce = 7414 時，
        Hash = 000031a57e9c7479cd6bf6f77c953b843eafad24b36cbded64c5c3af0970d658
    
---
 
### 生成區塊的Hash值

* 輸入區塊屬性與自訂的Nonce值，生成區塊的Hash值
* 
    1.  block_number = 1
    2.  transactions = Raheeem -> dog -> 20, dog -> cat -> 45
    3.  previous_hash = 0000000000000000000000000000000000000000000000000000000000000000    
    4.  Nonce = 2

```python
from hashlib import sha256
# SHA256函式
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

if __name__ == '__main__':
    # 區塊內容
    block_number = 1
    transactions = '''
    Raheem -> dog -> 20,
    dog -> cat -> 45
    '''
    previous_hash = '0' * 19
    nonce = 2

    text = str(block_number) + transactions + previous_hash + str(nonce)
    print(SHA256(text))
```

![](https://i.imgur.com/QUICatp.png)

* Hash = 3db3bdbd49052dd9c713e02f91c1e1bda1704b7732024a49d98277b632300cd9

---

### 挖礦

* Steps：
    1. 設定難度
    2. 建立新區塊
    3. 開始挖礦，猜測Nonce
    4. 猜測成功，得到新區塊的Hash值

* 輸入區塊屬性與難度 ( Difficulty )
* 
    1.  block_number = 2
    2.  transactions = Raheeem -> dog -> 20, dog -> cat -> 45
    3.  previous_hash = 3db3bdbd49052dd9c713e02f91c1e1bda1704b7732024a49d98277b632300cd9
    4.  Difficulty = 4

```python
import time 
from hashlib import sha256

class block():
    def __init__(self, block_number, transactions, previous_hash, difficulty):
        self.MAX_NONCE = 100000  # Nonce值的大小
        # 區塊屬性
        self.__block_number = str(block_number)
        self.__transactions = transactions
        self.__previous_hash = str(previous_hash)
        self.__blockContent = self.__block_number + self.__transactions + self.__previous_hash
        # 輸入的難度 = 生成的Hash值前有幾個零
        self.__prefix_zeros = difficulty
        self.__prefix_str = '0' * self.__prefix_zeros

    # SHA256產生Hash值
    def SHA256(self, text):
        return sha256(self.text.encode("ascii")).hexdigest()
    # 挖礦
    def mining(self):
        # 窮舉法 (猜測值從1開始測試)
        for nonce in range(self.MAX_NONCE):
            self.text = str(self.__blockContent) + str(nonce)  # 區塊內容 + 猜測值
            self.__new_hash = self.SHA256(self.text)           # 生成Hash值
            # 生成的Hash必須滿足設定的難度，若答案相符則挖礦成功
            # 輸入的難度 = 生成的Hash值前有幾個零 = 得到猜測值
            if self.__new_hash.startswith(self.__prefix_str):
                print(f"Successfully mined bitcoins with nonce value:{nonce}")
                return self.__new_hash
        # 答案不在設定好的猜測值範圍內，挖礦失敗
        raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")
    # 印出成功挖出的新區塊Hash值    
    def result(self):
        print(self.__new_hash)

if __name__ == '__main__':
    # 區塊編號
    block_number = 2
    # 交易內容
    transactions = '''
    Raheem -> dog -> 20,
    dog -> cat -> 45
    '''
    # 前一個區塊的Hash值
    pre_hash = '3db3bdbd49052dd9c713e02f91c1e1bda1704b7732024a49d98277b632300cd9'
    # 難度，代表生成的Hash值開頭有幾個0
    difficulty = 4
    # 建立新區塊
    newBlock = block(block_number, transactions, pre_hash, difficulty)
    
    start = time.time()                      # 計算挖掘時間
    print('Start mining')
    # 挖礦
    newBlock.mining()    
    
    total_time = str((time.time() - start))  # 計算挖掘時間
    print(f"End mining. Mining took: {total_time} seconds")
    # 印出成功挖出的新區塊Hash值
    newBlock.result()       
```

![](https://i.imgur.com/ucpb3jl.png)

* Difficulty = 4，得到Nonce = 7417
* Hash = 000031a57e9c7479cd6bf6f77c953b843eafad24b36cbded64c5c3af0970d658
* 所花時間 = 0.03 seconds
* Difficulty 難度越高，所需的算力與時間越多
* 計算速度取決於CPU算力
* 挖礦成功的機率取決於猜測Nonce的演算法

---

### 檢查Hash值

* 輸入區塊屬性與已經得到的Nonce值，可檢查該區塊的Hash與設定的難度是否一致
* 
    1.  block_number = 2
    2.  transactions = Raheeem -> dog -> 20, dog -> cat -> 45
    3.  previous_hash = 3db3bdbd49052dd9c713e02f91c1e1bda1704b7732024a49d98277b632300cd9
    4.  Nonce = 7417

```python
from hashlib import sha256
# SHA256函式
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

if __name__ == '__main__':
    # 區塊內容
    block_number = 2
    transactions = '''
    Raheem -> dog -> 20,
    dog -> cat -> 45
    '''
    previous_hash = '3db3bdbd49052dd9c713e02f91c1e1bda1704b7732024a49d98277b632300cd9'
    nonce = 7417

    text = str(block_number) + transactions + previous_hash + str(nonce)
    print(SHA256(text))
```

![](https://i.imgur.com/fVmjr4n.png)

* Hash = 000031a57e9c7479cd6bf6f77c953b843eafad24b36cbded64c5c3af0970d658
* 和挖擴程式生成的Hash值相同
