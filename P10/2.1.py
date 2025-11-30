def is_magic_square(matrix, n):
    target_sum = sum(matrix[0])

    # Проверяем суммы всех строк
    for i in range(n):
        if sum(matrix[i]) != target_sum:
            return False

    # Проверяем суммы всех столбцов
    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != target_sum:
            return False

    # Проверяем главную диагональ
    diag1 = sum(matrix[i][i] for i in range(n))
    if diag1 != target_sum:
        return False

    # Проверяем побочную диагональ
    diag2 = sum(matrix[i][n - 1 - i] for i in range(n))
    if diag2 != target_sum:
        return False

    return True


def main():
    # Чтение из файла
    with open('Викулин_У_253_vvod.txt', 'r') as f:
        lines = f.readlines()

    n = int(lines[0].strip())
    matrix = []
    for i in range(1, n + 1):
        row = list(map(int, lines[i].split()))
        matrix.append(row)

    # Проверка и запись результата
    with open('Викулин_У_253_vivod.txt', 'w') as f:
        if is_magic_square(matrix, n):
            f.write("Матрица является магическим квадратом\n")
        else:
            f.write("Матрица НЕ является магическим квадратом\n")


if __name__ == "__main__":
    main()