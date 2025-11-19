def to_8_digit_octal(n):
    octal = oct(n)[2:]
    return octal.zfill(10)

number = int(input("Введите неотрицательное целое число: "))
if number < 0:
    print("Ошибка: число должно быть неотрицательным")
else:
    octal_code = to_8_digit_octal(number)
    print(f"10-значный восьмеричный код: {octal_code}")