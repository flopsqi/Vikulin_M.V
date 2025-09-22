A = int(input('Введите число: '))
B = int(input('Введите число: '))
if A < B:
    for i in range(A,B+1):
        print(i,end='; ')
else:
    for i in range(A,B-1,-1):
        print(i,end='; ')