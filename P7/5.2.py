arr = []
for i in range(10):
    arr.append(int(input(f"Введите элемент {i+1}: ")))
unique_arr = []
for num in arr:
    if num not in unique_arr:
        unique_arr.append(num)
print("Массив без повторений:", unique_arr)