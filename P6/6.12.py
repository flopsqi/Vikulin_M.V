text = input('Введите текст: ')
words = text.split()
result_words = [word for word in words if word.endswith('я')]
print('Слова, оканчивающиеся на Я :')
for word in result_words:
    print(word)