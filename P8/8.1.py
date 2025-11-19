def is_divisible_by_its_digits(n):
    original = n
    while n > 0:
        digit = n % 10
        if digit == 0 or original % digit != 0:
            return False
        n //= 10
    return True

n = int(input("Введите число n: "))
print(f"Числа, не превосходящие {n}, которые делятся на каждую из своих цифр:")

found = False
for i in range(1, n + 1):
    if is_divisible_by_its_digits(i):
        print(i, end=' ')
        found = True

if not found:
    print("Таких чисел нет")
else:
    print()