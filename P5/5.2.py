n = int(input('Введите число: '))
divisor = 2
while n % divisor != 0:
    divisor += 1
print(divisor)