import matplotlib.pyplot as plt
import multiprocessing as mp
import time

def hashingv2(plaintext, length=32):
    file = open("hash-times.txt", "a")
    start_time = time.time()
    cardamom = len(plaintext)
    hash = []
    salt = 0
    pepper = 0
    counter = 0
    text = "abcdefghjiklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ)(*&%$#@!<?"

    for char in plaintext:
        pepper += ord(char) + pepper
        pepper -= ~ len(plaintext)

    while counter <= length:
        cardamom += pepper * cardamom & salt
        pepper += 2
        salt -= ~ len(plaintext)
        counter += 1
        pepper %= cardamom
    
    counter = 0
    plaintext = plaintext.encode()
    while counter <= length:
        cardamom = (salt << pepper) | (cardamom >> pepper)
        hash.append(text[(cardamom*salt*pepper) % len(text)])
        pepper += plaintext[counter % len(plaintext)]
        salt += 1
        counter += 1

    file.write(str(time.time() - start_time) + '\n')
    file.close()

def hashing(plaintext, length=32):
    file = open("hash-times.txt", "a")
    start_time = time.time()
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
    
    file.write(str(time.time() - start_time) + '\n')
    file.close()

arguments = []
file = open("hash-times.txt", "w")
file.close()

for i in range(1000):
    arguments.append("xg"*(i+1))

for i in range(1000//mp.cpu_count()):
    try:
        processes = []
        for j in range(mp.cpu_count()):
            processes.append(mp.Process(target=hashing, args=(arguments[i*mp.cpu_count()+j],)))
        for process in processes:
            process.start()
        for process in processes:
            process.join()
    except (KeyboardInterrupt or IndexError):
        for process in processes:
            process.terminate()
        break