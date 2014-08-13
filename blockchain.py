 class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the origin/genesis block
        self.new_block(previous_hash=1, proof=101)


    def new_block(self):
        # Create a new Block and add it to the chain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    
    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
        })
        
        return self.last_block['index'] + 1
    

    @staticmethod
    def hash(block):
         """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
        


    @property
    def last_block(self):
        # Return the last block of the chain
        return self.chain[-1]
