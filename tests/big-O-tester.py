import multiprocessing as mp
import time

def hashingv2(plaintext, length=32):
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

times = []
arguments = []

for i in range(1000):
    arguments.append("xg"*(i+1))

for i in range(1000):
    try:
        start_time = time.time()
        p = mp.Process(target=hashing, args=(arguments[i],))
        p.start()
        p.join()
        times.append(time.time()-start_time)
        if i % 100 == 0:
            print(i)
    except KeyboardInterrupt:
        break

file = open("hash-times.txt", "w")
for i in times:
    file.write(str(i) + '\n')
file.close()