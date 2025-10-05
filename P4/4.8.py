n = int(input("Введите натуральное число n (1-9): "))
if n < 1 or n > 9:
    print("Число должно быть от 1 до 9!")
else:
    stair = ""
    for i in range(1, n + 1):
        stair += str(i)
        print(stair)