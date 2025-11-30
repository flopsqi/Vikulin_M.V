def main():
    n = int(input("Введите порядок матрицы n: "))
    k = int(input("Введите номер строки k (от 0 до n-1): "))

    if k < 0 or k >= n:
        print("Неверный номер строки!")
        return

    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)

    diagonal_element = matrix[k][k]

    if diagonal_element == 0:
        print("Диагональный элемент равен 0, деление невозможно!")
        return

    for j in range(n):
        matrix[k][j] /= diagonal_element

    print("Преобразованная матрица:")
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()