import json
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
with open("dict.json", mode="w", encoding="utf-8") as write_file:
    json.dump(QUESTIONS, write_file, ensure_ascii=False, indent=4)