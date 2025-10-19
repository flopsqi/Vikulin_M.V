text = input('Введите текст: ')
max_n = 0
current = 0
for char in text:
    if char == 'н':
        current += 1
        max_n = max(max_n, current)
    else:
        current = 0
new_text = text.replace('!', '.')
print('Самая длинная последовательность H: ',max_n)
print('Преобразованная строка: ',new_text)