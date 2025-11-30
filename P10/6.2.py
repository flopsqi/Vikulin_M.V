def main():
    # Чтение из файла
    with open('Викулин_У_253_vvod.txt', 'r') as f:
        lines = f.readlines()

    N = int(lines[0].strip())
    if N % 2 == 0:
        with open('Викулин_У_253_vivod.txt', 'w') as f:
            f.write("N должно быть нечетным!\n")
        return

    matrix = []
    for i in range(1, N + 1):
        row = list(map(float, lines[i].split()))
        matrix.append(row)

    # Находим максимальный элемент на главной и побочной диагоналях
    max_val = matrix[0][0]
    max_i, max_j = 0, 0

    for i in range(N):
        # Главная диагональ
        if matrix[i][i] > max_val:
            max_val = matrix[i][i]
            max_i, max_j = i, i

        # Побочная диагональ
        if matrix[i][N - 1 - i] > max_val:
            max_val = matrix[i][N - 1 - i]
            max_i, max_j = i, N - 1 - i

    # Элемент на пересечении диагоналей
    center_i = center_j = N // 2

    # Меняем местами
    matrix[max_i][max_j], matrix[center_i][center_j] = matrix[center_i][center_j], matrix[max_i][max_j]

    # Запись в файл
    with open('Викулин_У_253_vivod.txt', 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')


if __name__ == "__main__":
    main()