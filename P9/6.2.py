def main():
    N = int(input("Введите порядок матрицы N (нечетное): "))
    if N % 2 == 0:
        print("N должно быть нечетным!")
        return

    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(N):
        row = list(map(float, input().split()))
        matrix.append(row)

    max_val = matrix[0][0]
    max_i, max_j = 0, 0

    for i in range(N):

        if matrix[i][i] > max_val:
            max_val = matrix[i][i]
            max_i, max_j = i, i

        if matrix[i][N - 1 - i] > max_val:
            max_val = matrix[i][N - 1 - i]
            max_i, max_j = i, N - 1 - i

    center_i = center_j = N // 2

    matrix[max_i][max_j], matrix[center_i][center_j] = matrix[center_i][center_j], matrix[max_i][max_j]

    print("Преобразованная матрица:")
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()