text = input('Введение исходного текста: ')
key = []
hash = []
m = len(text)
c = 0.1
# преобразование текста в цифры по таюлице ASCII.
for i in range(len(text)):
    text_element = text[i]
    key_element = ord(text_element)
    key.append(key_element)

for i in range(len(key)):
    key_element = key[i]
    hash_element = int(m * ((key_element * c) % 1))
    hash.append(hash_element)
print(key)
print(hash)






