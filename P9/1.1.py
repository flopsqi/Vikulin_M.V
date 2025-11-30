def main():
    N = int(input("Введите размер матрицы N: "))
    A = []
    print("Введите элементы матрицы построчно:")
    for i in range(N):
        row = list(map(int, input().split()))
        A.append(row)
    total_sum = 0
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i][j] > 0:
                total_sum += A[i][j]
                count += 1
    print(f"Сумма положительных элементов над главной диагональю: {total_sum}")
    print(f"Количество положительных элементов над главной диагональю: {count}")

if __name__ == "__main__":
    main()