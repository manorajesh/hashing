import jellyfish as jf

def hashing(plaintext, length=32):
    seed = 0
    hash = []
    salt = 0
    random_length_num = 1
    text = "abcdefghjiklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ)(*&%$#@!<>?"

    for char in plaintext:
        random_length_num += ord(char) + random_length_num
        random_length_num += ~ len(plaintext)

    while salt <= length:
        seed += ord(plaintext[salt % len(plaintext)]) + salt * random_length_num
        hash.append(text[(seed**salt*random_length_num) % len(text)])
        salt += 1
        random_length_num += 1
    return hash

plaintext1 = "xgxg"
plaintext2 = "xg"

print("".join(hashing(plaintext1)))
print("".join(hashing(plaintext2)))
print(jf.jaro_distance("".join(hashing(plaintext1)), "".join(hashing(plaintext2))))