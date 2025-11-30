def is_magic_square(matrix, n):
    target_sum = sum(matrix[0])

    for i in range(n):
        if sum(matrix[i]) != target_sum:
            return False

    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != target_sum:
            return False

    diag1 = sum(matrix[i][i] for i in range(n))
    if diag1 != target_sum:
        return False

    diag2 = sum(matrix[i][n - 1 - i] for i in range(n))
    if diag2 != target_sum:
        return False

    return True

def main():
    n = int(input("Введите порядок матрицы n: "))

    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    if is_magic_square(matrix, n):
        print("Матрица является магическим квадратом")
    else:
        print("Матрица НЕ является магическим квадратом")


if __name__ == "__main__":
    main()