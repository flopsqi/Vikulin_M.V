def main():
    # Чтение из файла
    with open('Викулин_У_253_vvod.txt', 'r') as f:
        lines = f.readlines()

    N, M = map(int, lines[0].split())
    B = []
    for i in range(1, N + 1):
        row = list(map(int, lines[i].split()))
        B.append(row)

    # Обработка каждой строки
    for i in range(N):
        row = B[i]
        min_val = min(row)
        max_val = max(row)

        min_index = row.index(min_val)
        max_index = row.index(max_val)

        # Меняем минимальный с последним
        row[min_index], row[-1] = row[-1], row[min_index]

        # Меняем максимальный с первым
        row[max_index], row[0] = row[0], row[max_index]

    # Запись в файл
    with open('Викулин_У_253_vivod.txt', 'w') as f:
        for row in B:
            f.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    main()