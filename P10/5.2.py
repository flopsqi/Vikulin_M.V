def main():
    # Чтение из файла
    with open('Викулин_У_253_vvod.txt', 'r') as f:
        lines = f.readlines()

    n, m = map(int, lines[0].split())
    matrix = []
    for i in range(1, n + 1):
        row = list(map(float, lines[i].split()))
        matrix.append(row)

    # Обработка каждой строки
    for i in range(n):
        min_val = min(matrix[i])
        min_index = matrix[i].index(min_val)

        # Заменяем минимальный элемент
        if min_val % 2 == 0:
            matrix[i][min_index] = 0
        else:
            matrix[i][min_index] = 1

    # Запись в файл
    with open('Викулин_У_253_vivod.txt', 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')


if __name__ == "__main__":
    main()