import random

n = int(input('Кустов: '))
garden_bed = []
for i in range(n):
    garden_bed.append(random.randint(1, 4242))
print('Грядка для проверки:', end = ' ')
print(*garden_bed)

x = int(input('Сейчас собираем с куста: '))
if x == n:
    print(f'Можно собрать ягод: {garden_bed[x-2] + garden_bed[x-1] + garden_bed[0]}')
elif x == 1:
    print(f'Можно собрать ягод: {garden_bed[n-1] + garden_bed[x-1] + garden_bed[x]}')
else:
    print(f'Можно собрать ягод: {garden_bed[x-2] + garden_bed[x-1] + garden_bed[x]}')