def mhash(plaintext, length=32):
    while len(plaintext) % length != 0:
        plaintext += "0"

    cardamom = len(plaintext)
    pepper = 0
    salt = 0
    hash = []

    plainbytes = plaintext.encode()

    for bytes in plainbytes:
        pepper += bytes + pepper
        pepper += ~ len(plaintext)
        hash.append(plainbytes[salt] + pepper)
        salt += 1

    salt = 0
    plainbytes2 = plaintext.encode()
    for i in plainbytes2:
        hash.append((salt << pepper) | (plainbytes2[salt] >> pepper))

    salt = -1
    for i in hash:
        hash[salt] += hash[len(hash) - salt]
        salt += 1

    return hash

print(mhash("ff"))