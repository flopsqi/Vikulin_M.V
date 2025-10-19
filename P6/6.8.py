text = input('Введите текст с точкой в конце: ').rstrip('.')
words = text.split()
count = len(words)
print('Количество слов в строке: ',count)