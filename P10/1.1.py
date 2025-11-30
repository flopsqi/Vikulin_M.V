def main():
    # Чтение из файла
    with open('Викулин_У_253_vvod.txt', 'r') as f:
        lines = f.readlines()

    N = int(lines[0].strip())
    A = []
    for i in range(1, N + 1):
        row = list(map(int, lines[i].split()))
        A.append(row)

    # Вычисление суммы и количества положительных элементов над главной диагональю
    total_sum = 0
    count = 0

    for i in range(N):
        for j in range(i + 1, N):
            if A[i][j] > 0:
                total_sum += A[i][j]
                count += 1

    # Запись в файл
    with open('Викулин_У_253_vivod.txt', 'w') as f:
        f.write(f"Сумма положительных элементов над главной диагональю: {total_sum}\n")
        f.write(f"Количество положительных элементов над главной диагональю: {count}\n")

if __name__ == "__main__":
    main()