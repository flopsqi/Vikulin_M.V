def main():
    # Чтение из файла
    with open('Викулин_У_253_vvod.txt', 'r') as f:
        lines = f.readlines()

    n = int(lines[0].strip())
    matrix = []
    for i in range(1, n + 1):
        row = list(map(float, lines[i].split()))
        matrix.append(row)

    # Формируем массив диагональных элементов и вычисляем след
    diagonal_elements = [matrix[i][i] for i in range(n)]
    trace = sum(diagonal_elements)

    # Преобразуем матрицу
    if trace != 0:
        for i in range(n):
            if i % 2 == 1:  # Четные строки (индексация с 0)
                for j in range(n):
                    matrix[i][j] /= trace

    # Запись в файл
    with open('Викулин_У_253_vivod.txt', 'w') as f:
        f.write(f"Диагональные элементы: {diagonal_elements}\n")
        f.write(f"След матрицы: {trace}\n")
        f.write("Преобразованная матрица:\n")
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')


if __name__ == "__main__":
    main()