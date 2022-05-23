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
        pepper += ~ len(plaintext)

    while counter <= length:
        cardamom += pepper * cardamom & salt
        pepper += 2
        salt += ~ len(plaintext)
        counter += 1
    
    counter = 0
    plaintext = plaintext.encode()
    while counter <= length:
        cardamom = (salt << pepper) | (cardamom >> pepper)
        hash.append(text[(cardamom*salt*pepper) % len(text)])
        pepper += plaintext[counter % len(plaintext)] & pepper
        salt += 1
        counter += 1
    
    return hash 

plaintext1 = "f"
plaintext2 = "ff"

print("".join(hashing(plaintext1)))
print("".join(hashing(plaintext2)))
print(jf.jaro_distance("".join(hashing(plaintext1)), "".join(hashing(plaintext2))))

counter = 0
while True:
    if hashing(plaintext1) == hashing(plaintext2):
        print("Collision found")
        print(plaintext1)
        print(plaintext2)
        print(counter)
        break
    else:
        plaintext2 += "f"
        counter += 1