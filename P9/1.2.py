def main():
    N = int(input("Введите количество строк N: "))
    M = int(input("Введите количество столбцов M: "))

    B = []
    print("Введите элементы матрицы построчно:")
    for i in range(N):
        row = list(map(int, input().split()))
        B.append(row)

    for i in range(N):
        row = B[i]
        min_val = min(row)
        max_val = max(row)

        min_index = row.index(min_val)
        max_index = row.index(max_val)

        row[min_index], row[-1] = row[-1], row[min_index]

        row[max_index], row[0] = row[0], row[max_index]

    print("Преобразованная матрица:")
    for row in B:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()