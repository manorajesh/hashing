import sys, os
import jellyfish as jf

## import hash.py by appending to PATH
sys.path.append(os.path.abspath("src/"))
import hash

plaintext1 = open('hash.txt', 'r').read()
plaintext1 = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
plaintext2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

print(hash.hashing(plaintext1))
print(hash.hashing(plaintext2))
print(jf.jaro_distance(hash.hashing(plaintext1), hash.hashing(plaintext2)))