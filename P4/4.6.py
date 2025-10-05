n = int(input("Введите натуральное число n: "))
if n < 0:
    print("Факториал определен только для натуральных чисел!")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"Факториал числа {n} равен {factorial}")