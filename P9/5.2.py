def main():
    n = int(input("Введите количество строк n: "))
    m = int(input("Введите количество столбцов m: "))

    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)

    for i in range(n):
        min_val = min(matrix[i])
        min_index = matrix[i].index(min_val)

        if min_val % 2 == 0:
            matrix[i][min_index] = 0
        else:
            matrix[i][min_index] = 1

    print("Новая матрица:")
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()