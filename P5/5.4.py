x = float(input('Введите число '))
y = float(input('Введите число '))
day = 1
while x < y:
    x *= 1.1
    day += 1
print('На',day,' день, спротсмен пробежит',y,'киллометров')