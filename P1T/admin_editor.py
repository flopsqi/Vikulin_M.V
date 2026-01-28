# admin_editor - скрипт для добавления вопросов администратором
import json

def add_question(filename):
    """Добавляет новый вопрос в JSON-файл"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            questions = json.load(f)
    except FileNotFoundError:
        questions = {}

    print("\nДобавление нового вопроса:")
    question = input("Введите текст вопроса: ")

    options = []
    print("Введите варианты ответов (первый вариант будет правильным):")
    for i in range(4):
        option = input(f"Вариант {i + 1}: ")
        options.append(option)

    questions[question] = options

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=4)

    print(f"Вопрос добавлен! Всего вопросов: {len(questions)}")


if __name__ == "__main__":
    add_question("dict.json")