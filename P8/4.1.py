def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

print("Деление дробей A/B ÷ C/D")
A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
D = int(input("Введите D: "))

# Деление дробей: (A/B) ÷ (C/D) = (A/B) * (D/C) = (A*D)/(B*C)
result_numerator = A * D
result_denominator = B * C

simplified_num, simplified_den = simplify_fraction(result_numerator, result_denominator)

print(f"Результат деления: {simplified_num}/{simplified_den}")