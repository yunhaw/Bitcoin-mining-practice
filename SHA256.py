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