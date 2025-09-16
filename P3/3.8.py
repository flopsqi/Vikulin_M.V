number1 = int(input('Введите значение: '))
number2 = int(input('Введите значение: '))
number3 = int(input('Введите значение: '))
if number1 == number2:
    if number1 == number3:
        print('3')
    else:
        print('2')
else:
    if number1 == number3:
        print('2')
    else:
        if number2 == number3:
            print('2')
        else:
            print('0')