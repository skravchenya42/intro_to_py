S = int(input("сумма: "))
P = int(input("произведение: "))

# в "эталонном" нет проверки инпута, хотя есть условие в задаче: просто полностью отсутствует вывод
if S == P or S + P > 2000:
    print("ввёл ерунду")
else:
    # а чтобы не совершать ошибок с двойным выводом, как в нашем Эталоне, костылим подсчет прохода цикла:
    cycle_count = 0
    for x in range(S):
        for y in range(P):
            if P == x*y and S == x+y:
                cycle_count += 1
                if cycle_count == 1:
                    print(f'x = {x}')
                    print(f'y = {y}')
                else:
                    break
