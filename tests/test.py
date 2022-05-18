import jellyfish as jf
import time
import base64

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
    return base64.b64encode("".join(hash).encode()).decode()

def lowercase_word(seed):
    word = ""
    while seed > 0:
        word += chr(seed % 26 + 97)
        seed = seed // 26
    return word

file = open("hash.txt", "w+")
file1 = open("hash.txt", "w+")
file2 = open("hash_collisions.txt", "w+")

number = 0
while number < 1000:
    number += 1
    file.write("".join(hashing(lowercase_word(number))) + " " + lowercase_word(number) + '\n')

print(f"Hashes created {time.asctime()}")

try:
    file.seek(0)
    counter = 0
    for line in file:
        for word in file1:
            if jf.jaro_distance(line, word) > 0.87 and line != word:
                file2.write(line + word + '\n')
        file1.seek(0)
        if counter % 500 == 0:
            print(counter, time.asctime())
        counter += 1
except KeyboardInterrupt:
    print("Keyboard interrupt")
    file.close()
    file1.close()
    file2.close()
    exit()

file.close()
file1.close()
file2.close()