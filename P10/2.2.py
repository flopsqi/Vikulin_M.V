def main():
    # Чтение из файла
    with open('Викулин_У_253_vvod.txt', 'r') as f:
        lines = f.readlines()

    N, M = map(int, lines[0].split())
    A = []
    for i in range(1, N + 1):
        row = list(map(int, lines[i].split()))
        A.append(row)

    # Переставляем первый и последний столбцы
    for i in range(N):
        A[i][0], A[i][-1] = A[i][-1], A[i][0]

    # Запись в файл
    with open('Викулин_У_253_vivod.txt', 'w') as f:
        for row in A:
            f.write(' '.join(map(str, row)) + '\n')


if __name__ == "__main__":
    main()