def main():
    n = int(input("Введите количество строк: "))
    m = int(input("Введите количество столбцов: "))

    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    row_sums = []
    for i in range(n):
        row_sum = sum(matrix[i])
        row_sums.append(row_sum)

    max_sum_index = row_sums.index(max(row_sums))
    min_sum_index = row_sums.index(min(row_sums))

    print(f"Строка с наибольшей суммой (индекс {max_sum_index}): {matrix[max_sum_index]}")
    print(f"Сумма: {row_sums[max_sum_index]}")
    print(f"Строка с наименьшей суммой (индекс {min_sum_index}): {matrix[min_sum_index]}")
    print(f"Сумма: {row_sums[min_sum_index]}")

if __name__ == "__main__":
    main()