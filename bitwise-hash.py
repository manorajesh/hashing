def hashing(plaintext, length=32):
    plainbytes = bytes(plaintext.encode())
    hash = []
    cardamom = 0

    for i in range(length):
        hash.append(plainbytes[i % len(plainbytes)])

    for byte in plainbytes:
        hash.append(~byte)
        hash.append(ord(plainbytes.decode()[1]))

    for i in range(len(hash)):
        hash[i] = (hash[i] << i) | (hash[i] >> i)

    for byte in plainbytes:
        cardamom += byte & 0x3274598

    for i in range(len(hash)):
        hash[i] = (hash[i] >> cardamom) | (hash[i] << cardamom)

    for i in range(length):
        hash[i] += hash[(len(hash)-i)%len(hash)]

    return hash

print(hashing("the"))