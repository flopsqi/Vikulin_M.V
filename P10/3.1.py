def is_symmetric(matrix, n):
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
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
        if is_symmetric(matrix, n):
            f.write("Матрица симметрична относительно главной диагонали\n")
        else:
            f.write("Матрица НЕ симметрична относительно главной диагонали\n")


if __name__ == "__main__":
    main()