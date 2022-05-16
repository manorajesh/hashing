import random
import string
from hash import hashing

def lowercase_word():
    word = ''
    random_word_length = random.randint(1, 5)
    while len(word) != random_word_length:
        word += random.choice(string.ascii_lowercase)
    return word
 
file1 = open("rainbowtabble.txt", "a")
while True:
    c = lowercase_word()
    file1.write("%s\t\t>\t%s\n" %(c, "".join(hashing(c))))