arr = [int(x) for x in input("Введите массив целых чисел через пробел: ").split()]
odd_numbers = [x for x in arr if x % 2 != 0]
if odd_numbers:
    odd_numbers.sort(reverse=True)
    print("Нечетные числа в порядке убывания:", odd_numbers)
else:
    print("Нечетных чисел нет")