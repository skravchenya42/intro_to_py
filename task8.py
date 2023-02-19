# Требуется решить древнюю задачу про шоколадку

m = int(input('m: '))
n = int(input('n: '))
k = int(input('сколько тебе нужно долек? '))
if (k%n==0 or k%m==0) and k<m*n:
    print("можно")
else:
    print("нельзя")