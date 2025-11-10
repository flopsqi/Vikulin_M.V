arr = []
for i in range(8):
    arr.append(int(input(f"Введите элемент {i+1}: ")))
for i in range(8):
    if arr[i] < 15:
        arr[i] *= 2
print("Преобразованный массив:", arr)