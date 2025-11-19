import math

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def quadrilateral_area(a, b, c, d, diagonal):
    area1 = triangle_area(a, b, diagonal)
    area2 = triangle_area(c, d, diagonal)
    return area1 + area2

print("Вычисление площади выпуклого четырехугольника")
a = float(input("Введите первую сторону: "))
b = float(input("Введите вторую сторону: "))
c = float(input("Введите третью сторону: "))
d = float(input("Введите четвертую сторону: "))
diag = float(input("Введите длину диагонали: "))

area = quadrilateral_area(a, b, c, d, diag)
print(f"Площадь четырехугольника: {area:.2f}")