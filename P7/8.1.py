arr = [int(x) for x in input("Введите список чисел через пробел: ").split()]
arr_sum = sum(arr)
arr_product = 1
for num in arr:
    arr_product *= num

print(f"Сумма элементов: {arr_sum}")
print(f"Произведение элементов: {arr_product}")