n = int(input('n: '))
m = int(input('m: '))
print()
list_n = []
list_m = []


def user_list(list, x):
    print(f'вводи список из {x} элементов: ')
    for i in range(x):
        list.append(input())
    return list


list_n = user_list(list_n, n)
list_n = set([int(i) for i in list_n])
list_m = user_list(list_m, m)
list_m = set([int(i) for i in list_m])
un_set = list_n.intersection(list_m)

print()
print('результат такой:', end=' ')
print(*un_set)
