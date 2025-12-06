# Блок Б, задание 3
def print_odd():
    x = int(input())
    if x == 0:
        return
    else:
        print(x)
        y = int(input())
        if y != 0:
            print_odd()
        else:
            return
print("Вводите натуральные числа (по одному в строке), завершите 0:")
print_odd()