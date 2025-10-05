n = int(input("Введите количество чисел из ряда Фибоначчи: "))
fib_number_a, fib_number_b = 0, 1
fib_numbers_sum = 0
for i in range(n):
    fib_numbers_sum += fib_number_a
    fib_number_a, fib_number_b = fib_number_b, fib_number_a + fib_number_b
print(f"Сумма первых {n} чисел ряда Фибоначчи: {fib_numbers_sum}")