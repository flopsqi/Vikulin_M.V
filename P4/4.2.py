numberA = int(input('Введите число: '))
numberB = int(input('Введите число: '))
if numberA < numberB:
    for i in range(numberA,numberB+1):
        print(i,end='; ')
else:
    for i in range(numberA,numberB-1,-1):
        print(i,end='; ')