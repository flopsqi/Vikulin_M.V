text = input('Введите текст со скобками: ')
start = text.find('(')
end = text.find(')')
if start != -1 and end != -1 and start < end:
    inside = text[start+1:end]
    print(f'Символы внутри скобок: {inside}')
else:
    print('Скобки не найдены или расположены некорректно')