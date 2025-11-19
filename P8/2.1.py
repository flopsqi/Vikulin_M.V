import math

def triangle_area(side):
    return (math.sqrt(3) / 4) * side ** 2

def hexagon_area(side):
    return 6 * triangle_area(side)

a = float(input("Введите длину стороны шестиугольника: "))
area = hexagon_area(a)
print(f"Площадь правильного шестиугольника со стороной {a}: {area:.2f}")