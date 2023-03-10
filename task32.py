import random

array = []
n = int(input('длина массива = '))

for i in range(n):
    array.append(random.randint(1, 4242))
print(array)
min = int(input('минимум диапазона = '))
max = int(input('максимум диапазона = '))
indexes = []
for i in range(n):
 if array[i] <= max and array[i] >= min:
    indexes.append(i)
print(*indexes)
