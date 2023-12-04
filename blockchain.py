import hashlib
import time
import random

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def calculate_randomx_hash(data, nonce):
    # Placeholder for RandomX hash calculation
    # Replace this with your RandomX hashing implementation
    random_seed = str(random.random())  # For illustration purposes
    value = data + str(nonce) + random_seed
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis", calculate_hash(0, "0", int(time.time()), "Genesis"))

class HybridProofBlock(Block):
    def __init__(self, index, previous_hash, timestamp, data, hash, capacity_proof, nonce):
        super().__init__(index, previous_hash, timestamp, data, hash)
        self.capacity_proof = capacity_proof
        self.nonce = nonce

def mine_hybrid_block(previous_block, data, capacity_proof):
    index = previous_block.index + 1
    timestamp = int(time.time())
    nonce = 0

    while True:
        candidate_block = create_hybrid_candidate_block(index, previous_block.hash, timestamp, data, capacity_proof, nonce)
        randomx_hash_result = calculate_randomx_hash(candidate_block.data, candidate_block.nonce)

        # Check if the hash meets certain criteria (e.g., starts with a certain number of zeros)
        if is_valid_randomx_hash(randomx_hash_result):
            return HybridProofBlock(
                index, previous_block.hash, timestamp, data, candidate_block.hash, capacity_proof, nonce
            )

        nonce += 1

def create_hybrid_candidate_block(index, previous_hash, timestamp, data, capacity_proof, nonce):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data) + str(capacity_proof) + str(nonce)
    hash_value = hashlib.sha256(value.encode('utf-8')).hexdigest()

    return {
        'index': index,
        'previous_hash': previous_hash,
        'timestamp': timestamp,
        'data': data,
        'capacity_proof': capacity_proof,
        'nonce': nonce,
        'hash': hash_value
    }

def is_valid_randomx_hash(hash_result):
    # You can define your own criteria for a valid RandomX hash
    return hash_result.startswith('0000')
