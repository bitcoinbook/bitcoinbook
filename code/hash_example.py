
# example of iterating a nonce in a hashing algorithm's input

import hashlib
    
text = "I am Satoshi Nakamoto"

for nonce in xrange(20):  # iterate nonce from 0 to 19
    input = text + str(nonce)  # add the nonce to the end of the text
    hash = hashlib.sha256(input).hexdigest() # calculate the SHA-256 hash of the input (text+nonce)
    print input, '=>',  hash # show the input and hash result