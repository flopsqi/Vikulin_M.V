arr = [int(x) for x in input("Введите массив целых чисел через пробел: ").split()]
sum_even = 0
product_odd = 1
for i in range(len(arr)):
    if i % 2 == 0:
        sum_even += arr[i]
    else:
        product_odd *= arr[i]
print(f"Сумма элементов с четными номерами: {sum_even}")
print(f"Произведение элементов с нечетными номерами: {product_odd}")