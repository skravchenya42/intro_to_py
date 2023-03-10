array = []
a = int(input('a = '))
d = int(input('d = '))
n = int(input('n = '))

for i in range(1,n+1):
    array.append(a + (i-1) * d)

print(array)