import jellyfish as jf
import time
import base64
from multiprocessing import Process
import multiprocessing as mp
import hashlib

## hashing function
def hashing(plaintext, length=32):
    seed = 0
    hash = []
    salt = 0
    cardamom = 1
    text = "abcdefghjiklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ)(*&%$#@!<>?"

    for char in plaintext:
        cardamom += ord(char) + cardamom
        cardamom += ~ len(plaintext)

    while salt <= length:
        seed += ord(plaintext[salt % len(plaintext)]) + salt * cardamom
        hash.append(text[(seed**salt*cardamom) % len(text)])
        salt += 1
        cardamom += salt
    return hash

## checking if sha has collisions
def sha(plaintext):
    return hashlib.sha256(plaintext.encode()).hexdigest()

## test if collisions are found properly
def hashing_test(plaintext, length=32):
    word = ""
    for i in range(length):
        word += "a"
    return word

## function to generate lowercase words
def lowercase_word(seed):
    word = ""
    seed *= 1
    while seed > 0:
        word += chr(seed % 26 + 97)
        seed = seed // 26
    return word

def multiple_letters(seed):
    word = ""
    while seed > 0:
        word += chr(seed % 26 + 97)
        seed -= 26
    return word

## function to find collisions
def thread_function(hashes):
    file2 = open("hash_collisions.txt", "a")
    try:
        counter = 0
        for line in hashes:
            for word in hashes:
                if jf.jaro_distance(line.split()[0], word.split()[0]) > 0.9 and line != word:
                    file2.write(line + word + '\n')

            if counter % 500 == 0:
                print(counter, time.asctime())
            counter += 1
        file2.close()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        file2.close()
        exit()

## check whether the threads are working
def thread_checker(hashes):
    global text_result
    for word in hashes:
        text_result.append(word)

## main
def main():
    file = open("hash.txt", "w+")
    file1 = open("hash.txt", "w+")
    file2 = open("hash_collisions.txt", "w+")

    ## Generate hashes
    number = 0
    hash_num = 10000
    while number < hash_num:
        number += 1
        file.write("".join(hashing(lowercase_word(number))) + " " + multiple_letters(number) + '\n')

    file.seek(0)
    print(f"{len(file.readlines())} Hashes created {time.asctime()}")

    ## Multi-threading starts here with division of the hash.txt file

    file.seek(0)
    text_buffer = file.readlines()

    start = 0
    for i in range(mp.cpu_count()):
        end = start + len(text_buffer) // mp.cpu_count()
        p = Process(target=thread_function, args=(text_buffer[start:end],))
        p.start()
        start = end

    for i in range(mp.cpu_count()):
        p.join()
    print("Done at " + time.asctime())

    file.close()
    file1.close()
    file2.close()

if __name__ == "__main__":
    main()