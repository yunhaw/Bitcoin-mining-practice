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