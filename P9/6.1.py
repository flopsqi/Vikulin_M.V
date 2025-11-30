def main():
    n = int(input("Введите порядок матрицы: "))

    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    print("Наибольшие элементы в каждой строке:")
    for i in range(n):
        max_in_row = max(matrix[i])
        print(f"Строка {i}: {max_in_row}")

    print("\nНаименьшие элементы в каждом столбце:")
    for j in range(n):
        min_in_col = min(matrix[i][j] for i in range(n))
        print(f"Столбец {j}: {min_in_col}")

if __name__ == "__main__":
    main()