def hashing(plaintext, length=50):
    plaintext = plaintext.encode('utf-8')
    ciphertext = 0
    H = [0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc]

    sum = 0
    for i, v in enumerate(plaintext):
        sum += v ^ i | H[i % 4]

    plaintext_length = len(plaintext)
    for i in range(length):
        ciphertext = ciphertext ^ plaintext[i % plaintext_length]
        ciphertext = ciphertext >> length | ciphertext << length
        ciphertext = ciphertext ^ sum << plaintext_length
    
    return hex(ciphertext % 0x27a4d9fcbaefde1d681707ff6922c3c2f3930436f6cf)[2:43]