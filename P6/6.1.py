text = input('Введите текст: ')
words = text.split()
count = sum(1 for word in words if word.lower().startswith('е'))
print(f'Количество слов начинающихся с E:',count)