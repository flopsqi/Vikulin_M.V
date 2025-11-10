arr = [int(x) for x in input("Введите массив целых чисел через пробел: ").split()]
positive_arr = [x for x in arr if x > 0]
other_arr = [x for x in arr if x <= 0]
print("Положительные элементы:", positive_arr)
print("Остальные элементы:", other_arr)