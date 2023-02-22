import random

n = int(input("вот столько монеток: "))
head = 0
tail = 0

for i in range(n):
    # почему, кстати, в эталонном решении юзер указывает, как лежит каждая монетка? "условие не подходит"
    side = int(random.randint(0,1))
    if side == 0:
        head += 1
    else:
        tail += 1
if head > tail:
    print(f'нужно перевернуть монеток: {tail}')

else:
    print(f'нужно перевернуть монеток: {head}')
