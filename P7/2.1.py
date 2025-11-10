n = int(input("Введите количество элементов массива: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Введите элемент {i+1}: ")))
min_element = min(arr)
min_index = arr.index(min_element)
print(f"Индекс минимального элемента: {min_index}")