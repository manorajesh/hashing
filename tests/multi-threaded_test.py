import jellyfish as jf
import time
import base64
from threading import Thread
import hashlib

def hashing(plaintext, length=32):
    seed = 0
    hash = []
    salt = 0
    random_length_num = 1
    text = "abcdefghjiklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ)(*&%$#@!<>?"

    for char in plaintext:
        random_length_num += ord(char) + random_length_num
        random_length_num = ~ random_length_num + (random_length_num << 15)
        random_length_num += random_length_num >> random_length_num
        random_length_num += ~ len(plaintext)

    while salt <= length:
        seed += ord(plaintext[salt % len(plaintext)]) + salt * random_length_num
        hash.append(text[(seed**salt*random_length_num) % len(text)])
        salt += 1
        random_length_num += 1
    return hash

def sha(plaintext):
    return hashlib.sha256(plaintext.encode()).hexdigest()

def hashing_test(plaintext, length=32):
    word = ""
    for i in range(length):
        word += "a"
    return word

def lowercase_word(seed):
    word = ""
    seed *= 1000000
    while seed > 0:
        word += chr(seed % 26 + 97)
        seed = seed // 26
    return word

file = open("hash.txt", "w+")
file1 = open("hash.txt", "w+")
file2 = open("hash_collisions.txt", "w+")

## Generate hashes

number = 0
hash_num = 100000
while number < hash_num:
    number += 1
    file.write("".join(hashing(lowercase_word(number))) + " " + lowercase_word(number) + '\n')

file.seek(0)
print(f"{len(file.readlines())} Hashes created {time.asctime()}")

def thread_function(hashes, file2):
    try:
        counter = 0
        for line in hashes:
            for word in hashes:
                if jf.jaro_distance(line, word) > 0.9 and line != word:
                    file2.write(line + word + '\n')

            if counter % 500 == 0:
                print(counter, time.asctime())
            counter += 1
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        file.close()
        file1.close()
        file2.close()
        exit()

## Multi-threading starts here with division of the hash.txt file

file.seek(0)
text_buffer = file.readlines()

thread1 = Thread(target=thread_function, args=(text_buffer[:hash_num // 10], file2))
thread2 = Thread(target=thread_function, args=(text_buffer[hash_num // 10:hash_num // 10 * 2], file2))
thread3 = Thread(target=thread_function, args=(text_buffer[hash_num // 10 * 2:hash_num // 10 * 3], file2))
thread4 = Thread(target=thread_function, args=(text_buffer[hash_num // 10 * 3:hash_num // 10 * 4], file2))
thread5 = Thread(target=thread_function, args=(text_buffer[hash_num // 10 * 4:hash_num // 10 * 5], file2))
thread6 = Thread(target=thread_function, args=(text_buffer[hash_num // 10 * 5:hash_num // 10 * 6], file2))
thread7 = Thread(target=thread_function, args=(text_buffer[hash_num // 10 * 6:hash_num // 10 * 7], file2))
thread8 = Thread(target=thread_function, args=(text_buffer[hash_num // 10 * 7:hash_num // 10 * 8], file2))
thread9 = Thread(target=thread_function, args=(text_buffer[hash_num // 10 * 8:hash_num // 10 * 9], file2))
thread10 = Thread(target=thread_function, args=(text_buffer[hash_num // 10 * 9:hash_num], file2))

try:
	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()
	thread5.start()
	thread6.start()
	thread7.start()
	thread8.start()
	thread9.start()
	thread10.start()
except KeyboardInterrupt:
	print("Keyboard interrupt")
	file.close()
	file1.close()
	file2.close()
	exit()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
thread9.join()
thread10.join()

print("Done at " + time.asctime())
file.close()
file1.close()
file2.close()
