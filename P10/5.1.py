def main():
    # Чтение из файла
    with open('Викулин_У_253_vvod.txt', 'r') as f:
        lines = f.readlines()

    n, m = map(int, lines[0].split())
    matrix = []
    for i in range(1, n + 1):
        row = list(map(int, lines[i].split()))
        matrix.append(row)

    # Сортировка каждой строки
    for i in range(n):
        matrix[i].sort()

    # Запись в файл
    with open('Викулин_У_253_vivod.txt', 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')


if __name__ == "__main__":
    main()