current = int(input('Введите число: '))
if current == 0:
    print(0)
else:
    max_count = 1
    count = 1
    while True:
        next_num = int(input('Введите число: '))
        if next_num == 0:
            break
        if next_num == current:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1
            current = next_num
    print('Наибольшее число подряд идущих элементов этой последовательности равных друг другу',max_count)