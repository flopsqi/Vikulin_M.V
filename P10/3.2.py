def main():
    # Чтение из файла
    with open('Викулин_У_253_vvod.txt', 'r') as f:
        lines = f.readlines()

    n, m = map(int, lines[0].split())
    matrix = []
    for i in range(1, n + 1):
        row = list(map(int, lines[i].split()))
        matrix.append(row)

    # Вычисляем суммы строк
    row_sums = []
    for i in range(n):
        row_sum = sum(matrix[i])
        row_sums.append(row_sum)

    # Находим строки с максимальной и минимальной суммой
    max_sum_index = row_sums.index(max(row_sums))
    min_sum_index = row_sums.index(min(row_sums))

    # Запись в файл
    with open('Викулин_У_253_vivod.txt', 'w') as f:
        f.write(f"Строка с наибольшей суммой (индекс {max_sum_index}): {matrix[max_sum_index]}\n")
        f.write(f"Сумма: {row_sums[max_sum_index]}\n")
        f.write(f"Строка с наименьшей суммой (индекс {min_sum_index}): {matrix[min_sum_index]}\n")
        f.write(f"Сумма: {row_sums[min_sum_index]}\n")


if __name__ == "__main__":
    main()