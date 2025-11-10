arr = [int(x) for x in input("Введите массив через пробел: ").split()]
min_index = arr.index(min(arr))
max_index = arr.index(max(arr))

arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
print("Массив после перестановки min и max:", arr)