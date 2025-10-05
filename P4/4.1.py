numberA = int(input('Введите число: '))
numberB = int(input('Введите число: '))
if numberA <= numberB:
    for i in range(numberA,numberB):
        print(i,end='; ')
else:
    print('Некорректные числа')