import  random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "Когда впервые было использовано слово 'Квиз'?": [
        "1781", "1871", "1771", "1881"
    ],
    "Какой тип данных в Python используется для целых чисел?": [
        "int", "float", "str", "bool"
    ],
    "Какое ключевое слово используется для условных выражений в Python?": [
        "if", "elif", "else", "for", "while"
    ],
    "Какой правильный способ доступа к последнему элементу списка в Python?": [
        "list[-1]", "list[-2]", "list[+1]", "list[0]",
    ],
    "Какой тип данных используется для хранения коллекции элементов, где каждый элемент индексируется по ключу в Python?": [
        "dict", "list", "tuple", "set"
    ],
}

def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

def get_answer(question, alternatives):
    print(question)
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nОтвет? ")) not in labeled_alternatives:
        print(f"Пожалуйста, введите один из следующих вариантов {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Правильно! ⭐")
        return 1
    else:
        print("Неверно")
        return 0

def run_quiz():
    questions = prepare_questions(
        QUESTIONS, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)

    print(f"\nВы набрали {num_correct} баллов из {num} возможных")

if __name__ == "__main__":
    run_quiz()