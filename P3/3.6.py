a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))
d = int(input('Введите число: '))
if not all(1 <= var <= 8 for var in [a, b, c, d]):
    print('Некорректные значения')
if a == c and b == d:
    print('Фигуры не могут стоять в одной клетке')
else:
    if (a + b) % 2 == (c + d) % 2:
            print('Да')
    else:
            print('Нет')