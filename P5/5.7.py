prev = int(input('Введите число: '))
count = 0
while prev != 0:
    next_num = int(input('Введите число: '))
    if next_num == 0:
        break
    if next_num > prev:
        count += 1
    prev = next_num
print(count,'элементов этой последовательности больше предыдущего элемента')