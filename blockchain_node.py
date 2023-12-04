import json
from flask import Flask, request

app = Flask(__name__)

# Placeholder for the blockchain
blockchain = []

# Placeholder for the miner
miner = None

@app.route('/mine', methods=['POST'])
def mine():
    data = request.json['data']
    mined_block = miner.mine(blockchain[-1], data)
    blockchain.append(mined_block.__dict__)
    return "Block mined and added to the blockchain."

@app.route('/blocks', methods=['GET'])
def get_blocks():
    return json.dumps(blockchain)

if __name__ == '__main__':
    # Set up the blockchain and miner
    from blockchain import create_genesis_block, mine_hybrid_block
    from miner import ProofOfCapacityMiner

    blockchain.append(create_genesis_block().__dict__)
    miner = ProofOfCapacityMiner("Your Proof of Capacity")

    # Run the Flask app
    app.run(port=5000)
