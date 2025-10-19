text = input('Введите предложение на английском: ')
words = text.split()
capitalized_words = [word.capitalize() for word in words]
new_text = ' '.join(capitalized_words)
print('Преобразованная строка: ',new_text)