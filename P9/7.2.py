def main():
    n = int(input("Введите порядок матрицы: "))

    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)

    diagonal_elements = [matrix[i][i] for i in range(n)]
    trace = sum(diagonal_elements)

    print(f"Диагональные элементы: {diagonal_elements}")
    print(f"След матрицы: {trace}")

    if trace != 0:
        for i in range(n):
            if i % 2 == 1:  # Четные строки (индексация с 0)
                for j in range(n):
                    matrix[i][j] /= trace

    print("Преобразованная матрица:")
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()