def is_point_inside_circle(x, y, a, b, R):
    distance_squared = (x - a)**2 + (y - b)**2
    return distance_squared <= R**2

print("Проверка точек на принадлежность окружности")
a = float(input("Введите координату a центра окружности: "))
b = float(input("Введите координату b центра окружности: "))
R = float(input("Введите радиус R окружности: "))

points = []
for i in range(3):
    print(f"Точка {i+1}:")
    x = float(input("Введите x координату: "))
    y = float(input("Введите y координату: "))
    points.append((x, y))

count_inside = 0
for i, (x, y) in enumerate(points, 1):
    if is_point_inside_circle(x, y, a, b, R):
        count_inside += 1
        print(f"Точка {i} находится внутри окружности")
    else:
        print(f"Точка {i} находится вне окружности")

print(f"\nВсего точек внутри окружности: {count_inside}")