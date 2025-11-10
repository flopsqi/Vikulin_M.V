n = int(input("Введите длину массива: "))
D = []
for i in range(n):
    D.append(int(input(f"Введите элемент {i+1}: ")))
sum_odd = 0
for i in range(1, n, 2):  # индексы 1, 3, 5...
    sum_odd += D[i]
print("Массив D:", D)
print(f"Сумма элементов с нечетными индексами: {sum_odd}")