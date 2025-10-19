text = input('Введите текст: ')
n = len(text)
half = n // 2
first_half = text[:half]
second_half = text[half:]
new_first_half = first_half.replace('п', '*')
result = new_first_half + second_half
print('Преобразованная строка: ',result)