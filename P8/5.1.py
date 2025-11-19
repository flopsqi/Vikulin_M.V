def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

print("Вычитание дробей A/B - C/D")
A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
D = int(input("Введите D: "))

# Вычитание дробей: (A/B) - (C/D) = (A*D - C*B)/(B*D)
result_numerator = A * D - C * B
result_denominator = B * D

simplified_num, simplified_den = simplify_fraction(result_numerator, result_denominator)

print(f"Результат вычитания: {simplified_num}/{simplified_den}")