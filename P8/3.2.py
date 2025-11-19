def sort_letters_in_words(text):
    words = text.split()
    sorted_words = []
    for word in words:
        sorted_word = ''.join(sorted(word))
        sorted_words.append(sorted_word)
    return ' '.join(sorted_words)

text = input("Введите строку: ")
result = sort_letters_in_words(text)
print("Результат:", result)