def is_symmetric(matrix, n):
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def main():
    n = int(input("Введите порядок матрицы n: "))

    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    if is_symmetric(matrix, n):
        print("Матрица симметрична относительно главной диагонали")
    else:
        print("Матрица НЕ симметрична относительно главной диагонали")


if __name__ == "__main__":
    main()