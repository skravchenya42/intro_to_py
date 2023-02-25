# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

import random

n = int(input('N = '))
array = [0]*n
relevant_x = array[0]
x = random.randint(1, n)

for i in range(len(array)):
    array[i] = random.randint(1, n)

dif = abs(x-array[0])

# в какую сторону самый близкий - в ТЗ не указано, так что делаю самостоятельный выбор: в бОльшую
# иначе самых близких будет 2 шт. во многих кейсах, а это противоречит заданию
for i in range(len(array)):
    if abs(x-array[i]) < dif:
        dif = abs(x-array[i])
        relevant_x = array[i]

print(*array)
print(f'X = {x}')
print(f'Ближе всего к Х: {relevant_x}')
