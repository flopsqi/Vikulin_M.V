a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))

if a<b:
    if a<c:
        print(f'Наименьшее число {a}')
    else:
        print(f'Наименьшее число {c}')
else:
    if b<c:
        print(f'Наименьшее число {b}')
    else:
        print(f'Наименьшее число {c}')