import random
import json
from string import ascii_lowercase

# Константы
NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_FILE = "dict.json"  # Имя файла с вопросами


def load_questions(filename):
    """Загружает вопросы из JSON-файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            questions = json.load(f)
        return questions
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        return {}
    except json.JSONDecodeError:
        print(f"Ошибка: файл '{filename}' содержит некорректный JSON.")
        return {}


def prepare_questions(questions, num_questions):
    """Выбирает случайные вопросы для теста"""
    if not questions:
        return []

    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def get_answer(question, alternatives):
    """Отображает вопрос и варианты, получает ответ пользователя"""
    print(f"\n{question}")

    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nОтвет? ").lower()) not in labeled_alternatives:
        print(f"Пожалуйста, введите одну из букв: {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]


def ask_question(question, alternatives):
    """Задает один вопрос и проверяет ответ"""
    correct_answer = alternatives[0]  # Правильный ответ - первый в списке
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)

    if answer == correct_answer:
        return 1
    else:
        print(f"Неверно. Правильный ответ: {correct_answer}")
        return 0


def run_quiz():
    """Основная функция запуска квиза"""
    # Загрузка вопросов из JSON-файла
    questions_dict = load_questions(QUESTIONS_FILE)

    if not questions_dict:
        print("Невозможно запустить квиз. Проверьте файл с вопросами.")
        return

    print(f"Загружено вопросов: {len(questions_dict)}")
    print(f"Будет задано: {min(NUM_QUESTIONS_PER_QUIZ, len(questions_dict))}")

    # Выбор случайных вопросов
    selected_questions = prepare_questions(
        questions_dict, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    if not selected_questions:
        print("Нет доступных вопросов для теста.")
        return

    # Запуск теста
    num_correct = 0
    for num, (question, alternatives) in enumerate(selected_questions, start=1):
        print(f"\n{'=' * 50}")
        print(f"Вопрос {num}:")
        num_correct += ask_question(question, alternatives)

    # Вывод результата
    print(f"\n{'=' * 50}")
    print(f"Тест завершен!")
    print(f"Вы набрали {num_correct} баллов из {len(selected_questions)} возможных")

    # Процент правильных ответов
    percentage = (num_correct / len(selected_questions)) * 100
    print(f"Результат: {percentage:.1f}%")


if __name__ == "__main__":
    run_quiz()