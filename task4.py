# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# никаких журавликов, у нас будут истребители, ведь классику знать надо!
# истребителей Зеро и торпедоносцев у нас поровну, а пикирующих бомбардировщиков - вдвое больше, чем Зеро и торпедоносцев вместе
s = int(input('сколько было истребителей? '))
x = s/6
if x%10==0:
    print(f"истребителей Зеро: {int(x)}")
    print(f"торпедоносцев: {int(x)}")
    print(f"пикирующих бомбардировщиков: {4*int(x)}")
else:
    print("не было столько истребителей, они бы нацело не поделились")