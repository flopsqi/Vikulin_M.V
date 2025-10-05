n = int(input("Введите натуральное число n: "))
if n < 0:
    print("Факториал определен только для натуральных чисел!")
else:
    factorial = 1
    factorial_sum = 0
    for i in range(1, n + 1):
        factorial *= i
        factorial_sum += factorial
    print(f"Сумма факториалов {factorial_sum}")