import jellyfish as jf

def hashing(plaintext, length=32):
    seed = 0
    hash = []
    salt = 0
    pepper = 0
    text = "abcdefghjiklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ)(*&%$#@!<>?"

    for char in plaintext:
        pepper += ord(char) + pepper
        pepper += ~ len(plaintext)

    while salt <= length:
        seed += ord(plaintext[salt % len(plaintext)]) + salt * pepper
        hash.append(text[(seed**salt*pepper) % len(text)])
        salt += 1
        pepper += salt
    return hash

plaintext1 = "f"
plaintext2 = "ff"

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

print("".join(hashing(plaintext1)))
print("".join(hashing(plaintext2)))
print(jf.jaro_distance("".join(hashing(plaintext1)), "".join(hashing(plaintext2))))