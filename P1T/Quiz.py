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

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

num_correct = 0
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nВопрос {num}:")
    print(question)
    correct_answer = alternatives[0]
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    )
    for label, alternative in labeled_alternatives.items():
        print(f" {label}) {alternative}")

    while (answer_label := input("\nОтвет? ")) not in labeled_alternatives:
        print(f"Пожалуйста, введите один из следующих вариантов {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        num_correct += 1
        print("⭐ Правильно! ⭐")
    else:
        print("Неверно")
print(f"\nВы набрали {num_correct} баллов из {num} возможных")