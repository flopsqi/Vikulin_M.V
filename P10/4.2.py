def main():
    # Чтение из файла
    with open('Викулин_У_253_vvod.txt', 'r') as f:
        lines = f.readlines()

    N = int(lines[0].strip())
    A = []
    for i in range(1, N + 1):
        row = list(map(int, lines[i].split()))
        A.append(row)

    # Замена элементов
    for i in range(N):
        for j in range(N):
            if A[i][j] < 0:
                A[i][j] = 0
            elif A[i][j] > 0:
                A[i][j] = 1

    # Запись в файл
    with open('Викулин_У_253_vivod.txt', 'w') as f:
        f.write("Преобразованная матрица:\n")
        for i in range(N):
            # Выводим только нижнюю треугольную часть
            row_str = ""
            for j in range(i + 1):
                row_str += str(A[i][j]) + " "
            f.write(row_str + "\n")


if __name__ == "__main__":
    main()