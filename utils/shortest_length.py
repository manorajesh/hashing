import sys, os

## import hash.py by appending to PATH
sys.path.append(os.path.abspath("src/"))
sys.path.append(os.path.abspath("tests/"))
import hash, test

shortest = ["", "", 0]
for i in range(100000):
    v = hash.hashing(test.lowercase_word(i+1))
    if len(v) > len(shortest[0]):
        shortest[0] = v
        shortest[1] = test.lowercase_word(i+1)
        shortest[2] = len(v)
print(shortest)