def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

gcd_result = gcd(a, b)
lcm_result = lcm(a, b)

print(f"НОД({a}, {b}) = {gcd_result}")
print(f"НОК({a}, {b}) = {lcm_result}")