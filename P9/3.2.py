def main():
    n = int(input("Введите количество строк n: "))
    m = int(input("Введите количество столбцов m: "))

    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)

    max_val = matrix[0][0]
    max_i, max_j = 0, 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_i, max_j = i, j

    if max_i != 0:
        matrix[0], matrix[max_i] = matrix[max_i], matrix[0]
        if max_i == 0:
            max_j = 0

    if max_j != 0:
        for i in range(n):
            matrix[i][0], matrix[i][max_j] = matrix[i][max_j], matrix[i][0]

    print("Преобразованная матрица:")
    for row in matrix:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()