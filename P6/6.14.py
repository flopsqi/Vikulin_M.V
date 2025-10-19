text = input('Введите текст: ')
words = text.split()
result_words = [word for word in words if word.startswith('а') or word.endswith('я')]
print('Слова начинающиеся на А или оканчивающиеся на Я:')
for word in result_words:
    print(word)