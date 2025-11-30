def main():
    N = int(input("Введите количество строк N: "))
    M = int(input("Введите количество столбцов M: "))

    A = []
    print("Введите элементы матрицы построчно:")
    for i in range(N):
        row = list(map(int, input().split()))
        A.append(row)

    for i in range(N):
        A[i][0], A[i][-1] = A[i][-1], A[i][0]

    print("Матрица после перестановки столбцов:")
    for row in A:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()