numberA = int(input('Введите число: '))
numberB = int(input('Введите число: '))
if numberA > numberB:
    for i in range(numberA,numberB-1,-1):
        if i%2 != 0:
            print(i)
else:
    print('Ошибка')