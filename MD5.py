import math

def addModuleTwo(x, y, module=2 ** 32):
    return ((x + y) % module)

def bitShift(s, sh):
    s = bin(s)[2:]
    s = int((s[sh:] + s[:sh]), 2)
    return s

def F(B, C, D):
    return (B & C | ~B & D)


def G(B, C, D):
    return (B & D | ~D & C)


def H(B, C, D):
    return (B ^ C ^ D)


def I(B, C, D):
    return (C ^ (B | ~D))

A = int('01234567', 16)
B = int('89abcdef', 16) 
C = int('fedcba98', 16) 
D = int('76543210', 16)

bufer = [A, B, C, D]
functions = [F, G, H, I]

text = input('Введение исходного текста: ')
text_in_numbers = ''

for i in range(len(text)):
    text_element = text[i]
    text_in_numbers_element = bin(ord(text_element))[2:]
    size = len(text_in_numbers_element)
    if size < 8:
        text_in_numbers_element = '0' * (8 - size) + text_in_numbers_element
    text_in_numbers += text_in_numbers_element

length = bin(len(text_in_numbers))[2:]
length = '0' * (64 - len(length)) + length

text_in_numbers += '1'
while len(text_in_numbers) % 512 != 448:
    text_in_numbers += '0'
text_in_numbers += length

m = []

k = 0
for i in range(0, len(text_in_numbers), 32):
    hex_number = ''
    for j in range(4):
        p = hex(int((text_in_numbers[i+8*j:i+j*8+8]), 2))[2:]
        if len(p) < 2:
            p = '0' + p
        hex_number += p
    m.append(int(hex_number, 16))

T = []
for i in range(1, 65):
    T.append(round(2 ** 32 * abs(math.sin(i))))

S = [[7, 12, 17, 22], [5, 9, 14, 20], [4, 11, 16, 23], [6, 10, 15, 21]]
K = [[], [], [], []]
K[0] = [int(i) for i in range(16)]
K[1] = [int(i) % 16 for i in range(1, 80, 5)]
K[2] = [int(i) % 16 for i in range(5, 53, 3)]
K[3] = [int(i) % 16 for i in range(0, 110, 7)]


ind_t = 0

for j in range(4):
    AA = bufer[0]
    BB = bufer[1]
    CC = bufer[2]
    DD = bufer[3]
    for k in range(16):
        bufer[0] = addModuleTwo(bufer[0], (functions[j](bufer[1], bufer[2], bufer[3])))
        bufer[0] = addModuleTwo(bufer[0], m[K[j][k]])
        bufer[0] = addModuleTwo(bufer[0], T[ind_t])
        bufer[0] = bitShift(bufer[0], S[j][k % 4])
        bufer[0] = addModuleTwo(bufer[1], bufer[0])
        bufer = bufer[3:4] + bufer[0:3]
        ind_t += 1
    bufer[0] = AA + bufer[0]
    bufer[1] = BB + bufer[1]
    bufer[2] = CC + bufer[2]
    bufer[3] = DD + bufer[3]


hexStr = '0x'
for i in bufer:
    h = hex(i)[2:]
    if len(h) < 8:
        h = '0' * (8 - len(h)) + h
    hexStr += h

print(hexStr)


            



