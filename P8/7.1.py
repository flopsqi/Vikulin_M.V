import math


def right_triangle_area(leg1, leg2):
    return 0.5 * leg1 * leg2


def rectangle_area(side1, side2):
    return side1 * side2


def quadrilateral_area(X, Y, Z, T):
    triangle_area = right_triangle_area(X, Y)
    hypotenuse = math.sqrt(X ** 2 + Y ** 2)

    # Для второй части четырехугольника используем формулу Герона
    p = (Z + T + hypotenuse) / 2
    second_triangle_area = math.sqrt(p * (p - Z) * (p - T) * (p - hypotenuse))

    return triangle_area + second_triangle_area


X = float(input("Введите сторону X: "))
Y = float(input("Введите сторону Y: "))
Z = float(input("Введите сторону Z: "))
T = float(input("Введите сторону T: "))

area = quadrilateral_area(X, Y, Z, T)
print(f"Площадь четырехугольника: {area:.2f}")