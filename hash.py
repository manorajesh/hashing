import jellyfish as jf
import time

def hashing(plaintext, length=55):
    plaintext = plaintext.encode('utf-8')
    ciphertext = 0
    H = [0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc]

    sum = 0
    for i, v in enumerate(plaintext):
        sum += v ^ i | H[i % 4]
        
    for i in H:
        sum = sum ^ i
        sum = sum << length | sum >> length

    plaintext_length = len(plaintext)
    for i in range(length):
        ciphertext = ciphertext ^ plaintext[i % plaintext_length]
        ciphertext = ciphertext >> length | ciphertext << length
        ciphertext = ciphertext ^ sum >> plaintext[i % plaintext_length]
    
    return hex(ciphertext % 100000000000000000000000000000010000000000000000000000000001)[2:46]


plaintext1 = open('hash.txt', 'r').read()
#plaintext1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
plaintext2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

print(hashing(plaintext1))
print(hashing(plaintext2))
print(jf.jaro_distance(hashing(plaintext1), hashing(plaintext2)))