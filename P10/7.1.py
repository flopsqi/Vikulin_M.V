def restore_symmetric_matrix(upper_triangle, n):
    matrix = [[0] * n for _ in range(n)]

    index = 0
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = upper_triangle[index]
            matrix[j][i] = upper_triangle[index]
            index += 1

    return matrix


def main():
    # Чтение из файла
    with open('Викулин_У_253_vvod.txt', 'r') as f:
        lines = f.readlines()

    n = int(lines[0].strip())
    total_elements = n * (n + 1) // 2

    # Читаем элементы верхнего треугольника
    upper_triangle = list(map(float, lines[1].split()))

    if len(upper_triangle) != total_elements:
        with open('Викулин_У_253_vivod.txt', 'w') as f:
            f.write("Неверное количество элементов!\n")
        return

    matrix = restore_symmetric_matrix(upper_triangle, n)

    # Запись в файл
    with open('Викулин_У_253_vivod.txt', 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')


if __name__ == "__main__":
    main()