number = int(input('Введите число: '))
numbers = range(number)
for i in numbers:
numbersProd = sum(pow(numbers,3))
print(numbersProd)