def pow(a, b):
    if b == 1:
        return a
    if b !=1:
        return pow(a, b - 1)*a
    
a = int(input('a = '))
b = int(input('b = '))
print(pow(a,b))