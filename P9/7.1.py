def restore_symmetric_matrix(upper_triangle, n):
    matrix = [[0] * n for _ in range(n)]

    index = 0
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = upper_triangle[index]
            matrix[j][i] = upper_triangle[index]
            index += 1

    return matrix

def main():
    n = int(input("Введите порядок матрицы n: "))

    total_elements = n * (n + 1) // 2
    print(f"Введите {total_elements} элементов верхнего треугольника (по строкам):")

    upper_triangle = list(map(float, input().split()))

    if len(upper_triangle) != total_elements:
        print("Неверное количество элементов!")
        return

    matrix = restore_symmetric_matrix(upper_triangle, n)

    print("Восстановленная матрица:")
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()