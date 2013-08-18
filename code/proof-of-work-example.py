
# example of proof-of-work algorithm

import hashlib
import time

max_nonce = 1000000000  # 1 billion

def proof_of_work(header, difficulty):
    
    target = 2<<(256-difficulty)
    
    for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(header)+str(nonce)).hexdigest()
        
        if long(hash_result, 16) < target:
            print "Success with nonce %d" % nonce
            print "Hash is %s" % hash_result
            return nonce
            
    print "Failed after %d (max_nonce) tries" % nonce
    return nonce

    
if __name__ == '__main__':
    
    difficulty = 24
    
    print "Difficulty: %d" % difficulty
    
    print "Starting search..."
    start_time = time.time()
    
    nonce = proof_of_work('test header', difficulty) # 5 bits of difficulty
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print "Elapsed Time: %.2f seconds" % elapsed_time
    
    if elapsed_time > 0:
        hash_power = float(long(nonce)/elapsed_time)
        print "Hashing Power: %ld hashes per second" % hash_power
    
    
    