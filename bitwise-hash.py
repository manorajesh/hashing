import base64
import zlib
import bitstring as bs
import jellyfish as jf

def compress(data, length):
    counter = 0
    data1 = 0
    while counter < length:
        data1 += data // 2
        data -= data1
        counter += 1

    data = zlib.compress(bytes(data % 10000000)).hex()
    data = data.replace("0", "")
    return data


input = 'lorem ipsum dolor sit amet'

bit_contents = bs.BitArray(input.encode('utf-8'))
for i in range(len(bit_contents)):
    bit_contents[i] = not bit_contents[i]

while len(bit_contents) % 64 != 0:
    bit_contents.append('0b0')

bit_contents = str(bit_contents.bin)
bit_contents2 = bs.BitArray(bit_contents.encode('utf-8'))
bit_contents2 = int(str(bit_contents2.bin))

for i in range(len(bit_contents)*64):
    bit_contents2 ^= (1 << i)

bit_contents2 = compress(bit_contents2, 32)
print(bit_contents2)