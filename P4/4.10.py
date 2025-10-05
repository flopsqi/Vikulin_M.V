n = int(input("Введите количество чисел: "))
k = int(input("Введите начальный порядковый номер: "))
fib_number_a, fib_number_b = 0, 1
fib_numbers_sum = 0
fib_numbers_count = 0
for i in range(1, k + n):
    if i >= k:
        fib_numbers_sum += fib_number_a
        fib_numbers_count += 1
    fib_number_a, fib_number_b = fib_number_b, fib_number_a + fib_number_b
    if fib_numbers_count >= n:
        break
print(f"Сумма чисел ряда Фибоначчи, начиная с {k}: {fib_numbers_sum}")