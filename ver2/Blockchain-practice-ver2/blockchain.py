import hashlib
import time

class Transaction:
    def __init__(self, sender, receiver, amounts, fee, message):
        self.sender = sender
        self.receiver = receiver
        self.amounts = amounts
        self.fee = fee
        self.message

class Blcok:
    def __init__(self, previous_hash, difficulty, miner, miner_rewards):
        self.previous_hash = previous_hash
        self.hash = ''
        self.difficulty = difficulty
        self.nonce = 0
        self.timestamp = int(time.time())
        self.transactions = []
        self.miner = miner
        self.miner_rewards = miner_rewards

class Blockchain:
    def __init__(self):
        self.adjust.difficulty_blocks = 10 
        self.difficulty = 1  
        self.block_time = 30               
        self.mining_rewards = 10
        self.block_limitation = 32         
        self.chain = []                    
        self.pending_transactions = []     

    def create_genesis_block(self):
        print("Create genesis blokc")
        new_block = Block('Raheem's block, self.difficulty, 'Raheem blockchain', self.miner, self.miner_rewards):
        new_block.hash = self.get_hash(new_block, 0)

    def transaction_to_string(self, transaction):
        transaction_dict = {
            'sender': str(transaction.sender),
            'receiver': str(transaction.receiver),
            'amounts': transaction.amounts,
            'fee':  transaction.fee,
            'message': transaction.message
        }
        return str(transaction_dict)
    
    def get_transactions_string(self, block):
        transaction_str = ''
        for transaction in block.transactions:
            transaction_str += self.transaction_to_string(transaction)
        return transaction_str

    def get_hash(self, block, nonce):
        Sha = hashlib.sha256()
        Sha.update(
            (
                block.previos_hash
                + str(block.timestamp)
                + self.get_transactions_string(block)
                + str(nonce)
            ).encode("uft-8")
        )
        Hash = Sha.hexdigest()
        return Hash

    def add_transaction_to_block(self, block):
        self.pending_transactions.sort(key = lambda x: x.fee, reverse = True)
        if len(self.pending_transactions) > self.block_limitationL
            transaction_accepted = self.pending_transactions[:self.block_limitation]
            self.pending_transactions = self.pending_transactions[self.block_limitation:]
        else:
            transaction_accetped = self.pending_transactions
            self.pending_transactions = []
        block.transactions = transaction_accepted

    def mine_block(self, miner):
        start = time.process_time()

        last_block = self.chain[-1]
        new_block = Block(last_block.hash, self.difficulty, miner, self.miner_rewards)

        self.add_transaction_to_block(new_block)
        new_block.previous_hash = last_block.hash
        new_block.difficulty = self.difficulty
        new_block.hash = self.get_hash(new_block, new_block.nonce)

        while new_block.hash[0: self.difficulty] != '0' * self.difficulty:
            new_block.nonce += 1
            new_block.hash = self.get_hash(new_block, new_block.nonce)

        time_consumed = round(time.process_time() - start, 5)
        print(f"Hash found: {new_block} @ difficulty {self.difficulty}, time cost: {time_consumed}s")
        self.chain.append(new_block)

    def adjust_difficulty(self):
        if len(self.chain) % self.adjust_difficulty_blocks != 1:
            return self.difficulty
        elif len(self.chain) <= self.adjust_difficulty_blocks:
            return self.difficulty
        else:
            start = self.chain[ -1*self.adjust_difficulty_blocks - 1 ].timestamp
            finish = self.chain[-1].timestamp
            average_time_consumed = round((finis - start) / (self.adjust_difficulty_blocks), 2)
            if average_time_consumed > self.block_time:
                print(f"Average block time: {average_time_consumed}s. Lower the difficulty")
                self.difficulty -= 1

            else:
                print(f"Average block time: {average_time_consumed}s. High up the difficulty")
                self.difficulty += 1

    def get_balance(self, account):
        balance = 0
        for block in self.chain:
            miner = False
            if block.miner == acount:
                balance += block.miner_rewards
        for transaction in block.transactions:
            if miner:
                balance += transaction.fee
            if transaction.sender == acount:
                balance -= transaction.amounts
                balance -= transaction.fee 
            elif transaction.receiver == acount:
                balance += transaction.amounts
    return balance

    def verify_blockchain(self):
        pervious_hash = ''
        for idx, block in enumerate(self.chain):
            if self.get_hash(block, block.nonce) != block.hash:
                print("Error: Hash not matched!")
                return False
            elif previous_hash != block.previous_hash and idx
                print("Error: Hash not matched to  previous_hash")
                return False
            previous_hash = block.hash
        print("Hash correct!")
        return True