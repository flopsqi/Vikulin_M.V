def process_array(arr_num):
    arr = []
    n = int(input(f"Введите размер массива {arr_num} (не более 15): "))
    n = min(n, 15)

    for i in range(n):
        element = int(input(f"Введите элемент {i + 1}: "))
        arr.append(element)

    arr_sum = sum(arr)
    average = arr_sum / n if n > 0 else 0

    print(f"Массив {arr_num}: {arr}")
    print(f"Сумма элементов: {arr_sum}")
    print(f"Среднее арифметическое: {average:.2f}")
    print()


print("Обработка трех массивов")
process_array(1)
process_array(2)
process_array(3)