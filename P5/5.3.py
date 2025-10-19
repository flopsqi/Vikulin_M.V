n = int(input('Введите число'))
if n > 0:
    power = 1
    exponent = 0
    while power * 2 <= n:
        power *= 2
        exponent += 1
    print('Степень равна' ,power,'при показатели степени' ,exponent)
else:
    print('N должно быть натуральным числом')