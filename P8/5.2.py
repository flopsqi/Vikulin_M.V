def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

number = int(input("Введите число: "))
divisors = find_divisors(number)
print("Делители числа:", ' '.join(map(str, divisors)))