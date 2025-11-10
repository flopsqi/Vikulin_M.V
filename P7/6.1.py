arr = []
for i in range(10):
    arr.append(int(input(f"Введите элемент {i+1}: ")))
average = sum(arr) / 10
max_element = max(arr)

count_less_max = sum(1 for x in arr if x < max_element)
count_greater_avg = sum(1 for x in arr if x > average)

print(f"Количество элементов меньших максимального ({max_element}): {count_less_max}")
print(f"Количество элементов больших среднего ({average:.2f}): {count_greater_avg}")