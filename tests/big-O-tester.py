import matplotlib.pyplot as plt
import multiprocessing as mp
import time

from click import argument

def hashing(plaintext, length=32):
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
    print("".join(hash))

times = []
arguments = []

for i in range(100):
    arguments.append("xg"*(i+1))


for i in range(100):
    try:
        start_time = time.time()
        p = mp.Process(target=hashing, args=(arguments[i],))
        p.start()
        p.join()
        times.append(time.time()-start_time)
    except KeyboardInterrupt:
        break

plt.plot(times)
plt.ylabel("Time")
plt.show()