# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм
# 'Парам пам-пам' - есть ритм, 'Пам парам' - нет ритма

poem_list = input('стих: ').lower().split()
vows_count_list = list(map(lambda str: sum(1 for i in str if i in 'аяуюоеёэиы'), poem_list))
if len(set(vows_count_list)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам') 