def main():
    # Чтение из файла
    with open('Викулин_У_253_vvod.txt', 'r') as f:
        lines = f.readlines()

    n = int(lines[0].strip())
    k = int(lines[1].strip())

    if k < 0 or k >= n:
        with open('Викулин_У_253_vivod.txt', 'w') as f:
            f.write("Неверный номер строки!\n")
        return

    matrix = []
    for i in range(2, 2 + n):
        row = list(map(float, lines[i].split()))
        matrix.append(row)

    diagonal_element = matrix[k][k]

    if diagonal_element == 0:
        with open('Викулин_У_253_vivod.txt', 'w') as f:
            f.write("Диагональный элемент равен 0, деление невозможно!\n")
        return

    # Делим элементы k-й строки на диагональный элемент
    for j in range(n):
        matrix[k][j] /= diagonal_element

    # Запись в файл
    with open('Викулин_У_253_vivod.txt', 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')


if __name__ == "__main__":
    main()