def main():
    n = int(input("Введите количество строк n: "))
    m = int(input("Введите количество столбцов m: "))

    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    for i in range(n):
        matrix[i].sort()

    print("Отсортированная матрица:")
    for row in matrix:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()