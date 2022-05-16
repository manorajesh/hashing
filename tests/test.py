import random
import string

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

def lowercase_word():
    word = ''
    random_word_length = random.randint(1, 5)
    while len(word) != random_word_length:
        word += random.choice(string.ascii_lowercase)
    return word
 
file1 = open("rainbowtabble.txt", "a")
while True:
    c = lowercase_word()
    file1.write("%s\t\t\t>\t\t%s\n" %(c, "".join(hashing(c))))