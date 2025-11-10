arr = [int(x) for x in input("Введите массив целых чисел через пробел: ").split()]
max_element = max(arr)
max_index = arr.index(max_element)
print(f"Максимальный элемент: {max_element}")
print(f"Порядковый номер: {max_index + 1}")