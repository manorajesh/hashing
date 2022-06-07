import jellyfish as jf
import time
import base64
from multiprocessing import Process
import multiprocessing as mp
import hashlib

## hashing function
def hashing(plaintext, length=55):
    plaintext = plaintext.encode('utf-8')
    ciphertext = 0
    H = [0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc]

    sum = 0
    for i, v in enumerate(plaintext):
        sum += v ^ i | H[i % 4]
        
    for i in H:
        sum = sum ^ i
        sum = sum << length | sum >> length

    plaintext_length = len(plaintext)
    for i in range(length):
        ciphertext = ciphertext ^ plaintext[i % plaintext_length]
        ciphertext = ciphertext >> length | ciphertext << length
        ciphertext = ciphertext ^ sum >> plaintext[i % plaintext_length]
    
    return hex(ciphertext % 100000000000000000000000000000010000000000000000000000000001)[2:46]

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
        file.write(hashing(multiple_letters(number)) + " " + multiple_letters(number) + '\n')

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