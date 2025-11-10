arr = []
for i in range(10):
    arr.append(int(input(f"Введите элемент {i+1}: ")))

sum_greater_5 = sum(x for x in arr if x > 5)
print(f"Сумма чисел больших 5: {sum_greater_5}")