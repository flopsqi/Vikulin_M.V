import math

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

print("Сравнение гипотенуз двух прямоугольных треугольников")

print("Первый треугольник:")
a1 = float(input("Введите первый катет: "))
b1 = float(input("Введите второй катет: "))

print("Второй треугольник:")
a2 = float(input("Введите первый катет: "))
b2 = float(input("Введите второй катет: "))

hyp1 = hypotenuse(a1, b1)
hyp2 = hypotenuse(a2, b2)

print(f"\nГипотенуза первого треугольника: {hyp1:.2f}")
print(f"Гипотенуза второго треугольника: {hyp2:.2f}")

if hyp1 > hyp2:
    print("Гипотенуза первого треугольника больше")
elif hyp2 > hyp1:
    print("Гипотенуза второго треугольника больше")
else:
    print("Гипотенузы равны")