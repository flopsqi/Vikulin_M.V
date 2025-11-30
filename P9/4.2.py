def main():
    N = int(input("Введите порядок матрицы N: "))

    A = []
    print("Введите элементы матрицы построчно:")
    for i in range(N):
        row = list(map(int, input().split()))
        A.append(row)

    for i in range(N):
        for j in range(N):
            if A[i][j] < 0:
                A[i][j] = 0
            elif A[i][j] > 0:
                A[i][j] = 1

    print("Преобразованная матрица:")
    for i in range(N):
        row_str = ""
        for j in range(i + 1):
            row_str += str(A[i][j]) + " "
        print(row_str)


if __name__ == "__main__":
    main()