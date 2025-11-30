def main():
    # Чтение из файла
    with open('Викулин_У_253_vvod.txt', 'r') as f:
        lines = f.readlines()

    n = int(lines[0].strip())
    matrix = []
    for i in range(1, n + 1):
        row = list(map(int, lines[i].split()))
        matrix.append(row)

    # Находим наибольшие элементы в каждой строке
    max_in_rows = []
    for i in range(n):
        max_in_rows.append(max(matrix[i]))

    # Находим наименьшие элементы в каждом столбце
    min_in_cols = []
    for j in range(n):
        min_in_col = min(matrix[i][j] for i in range(n))
        min_in_cols.append(min_in_col)

    # Запись в файл
    with open('Викулин_У_253_vivod.txt', 'w') as f:
        f.write("Наибольшие элементы в каждой строке:\n")
        for i in range(n):
            f.write(f"Строка {i}: {max_in_rows[i]}\n")

        f.write("\nНаименьшие элементы в каждом столбце:\n")
        for j in range(n):
            f.write(f"Столбец {j}: {min_in_cols[j]}\n")


if __name__ == "__main__":
    main()