# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

n = int(input('N = '))
a = [0]*n
count_x = 0
x = random.randint(1, n)

for i in range(n):
    a[i] = random.randint(1, n)

print(*a)
print(f'X = {x}')

for i in range(n):
    if a[i] == x:
        count_x += 1

print(f'X встретился раз: {count_x}')
