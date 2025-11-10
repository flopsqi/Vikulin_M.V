arr = []
for i in range(10):
    arr.append(int(input(f"Введите элемент {i+1}: ")))
print("Пары отрицательных чисел, стоящих рядом:")
for i in range(9):
    if arr[i] < 0 and arr[i+1] < 0:
        print(f"({arr[i]}, {arr[i+1]})")