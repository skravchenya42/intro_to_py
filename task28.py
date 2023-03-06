def sum(a, b):
    if a == 0:
        return b
    elif  b == 0:
        return a
    elif a <= b:
        return sum(a-1, b+1)
    else:
        return sum(a+1, b-1)


a = int(input('a = '))
b = int(input('b = '))
print(sum(a, b))
