import jellyfish as jf

def hashing(plaintext, length=32):
    cardamom = len(plaintext)
    hash = []
    salt = 0
    pepper = 0
    counter = 0
    text = "abcdefghjiklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ)(*&%$#@!<?"

    for char in plaintext:
        pepper += ord(char) + pepper
        pepper -= ~ len(plaintext)

    while counter <= length:
        cardamom += pepper * cardamom & salt
        pepper += 2
        salt -= ~ len(plaintext)
        counter += 1
        pepper %= cardamom
    
    counter = 0
    plaintext = plaintext.encode()
    while counter <= length:
        cardamom = (salt << pepper) | (cardamom >> pepper)
        hash.append(text[(cardamom*salt*pepper) % len(text)])
        pepper += plaintext[counter % len(plaintext)]
        salt += 1
        counter += 1
    return hash 

plaintext1 = "xg"
plaintext2 = "xgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxgxg"

print("".join(hashing(plaintext1)))
print("".join(hashing(plaintext2)))
print(jf.jaro_distance("".join(hashing(plaintext1)), "".join(hashing(plaintext2))))