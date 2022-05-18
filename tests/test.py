from ctypes.wintypes import WORD
import jellyfish as jf

def hashing(plaintext, length=32):
    seed = 0
    hash = []
    salt = 0
    random_length_num = 1
    text = "abcdefghjiklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ)(*&%$#@!"

    for char in plaintext:
        random_length_num += ord(char)

    while salt <= length:
        seed += ord(plaintext[salt % len(plaintext)]) + salt * random_length_num
        hash.append(text[(seed**salt*random_length_num) % len(text)])
        salt += 1
        random_length_num += 1
    return hash

def lowercase_word(seed):
    word = ""
    while seed > 0:
        word += chr(seed % 26 + 97)
        seed = seed // 26
    return word



file = open("hash.txt", "r+")
file1 = open("hash.txt", "r+")
file2 = open("hash_collisions.txt", "w+")

number = 0
while number < 10:
    number += 1
    file.write("".join(hashing(lowercase_word(number))) + '\n')

file.seek(0)
counter = 0
for line in file:
    for word in file1:
        if jf.jaro_distance(line, word) > 0.95 and line != word:
            file2.write(line + " -> " + word + '\n')
    counter += 2
    file.seek(counter)
    file1.seek(0)