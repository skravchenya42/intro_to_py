def pow(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    if b !=1:
        return pow(a, b - 1)*a
    
a = int(input('a = '))
b = int(input('b = '))
print(pow(a,b))