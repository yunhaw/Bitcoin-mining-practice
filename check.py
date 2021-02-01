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