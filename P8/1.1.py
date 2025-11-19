import math

def circle_area(radius):
    return math.pi * radius ** 2

def triangle_area(base, height):
    return 0.5 * base * height

def rectangle_area(length, width):
    return length * width

print("Вычисление площадей геометрических фигур")
print("1. Круг")
print("2. Треугольник")
print("3. Прямоугольник")

choice = int(input("Выберите фигуру (1-3): "))

if choice == 1:
    r = float(input("Введите радиус круга: "))
    print(f"Площадь круга: {circle_area(r):.2f}")
elif choice == 2:
    b = float(input("Введите основание треугольника: "))
    h = float(input("Введите высоту треугольника: "))
    print(f"Площадь треугольника: {triangle_area(b, h):.2f}")
elif choice == 3:
    l = float(input("Введите длину прямоугольника: "))
    w = float(input("Введите ширину прямоугольника: "))
    print(f"Площадь прямоугольника: {rectangle_area(l, w):.2f}")
else:
    print("Неверный выбор")