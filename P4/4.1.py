A = int(input('Введите число: '))
B = int(input('Введите число: '))
if A <= B:
    for i in range(A,B):
        print(i,end='; ')
else:
    print('Некорректные числа')