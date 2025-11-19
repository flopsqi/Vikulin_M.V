def rectangle_area(length, width):
    return length * width

print("Вычисление площадей трех прямоугольников")

for i in range(3):
    print(f"\nПрямоугольник {i+1}:")
    l = float(input("Введите длину: "))
    w = float(input("Введите ширину: "))
    area = rectangle_area(l, w)
    print(f"Площадь: {area:.2f}")