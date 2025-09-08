age = int(input("Enter your age: "))
class_age = 16-age
if 0<age<75:
    if age >= 16:
            name = input("Enter your name: ")
            if name != 'Иван':
                pass
                print('Поздравляем вы поступили в ВГУИТ')
            else:
                print('Иванов тут не любят')
    elif class_age>9:
            print('Сначала нужно окончить 9 лет школы!')
    elif 1<class_age<5:
        print(f'Сначала нужно окончить {class_age} года школы!')
    elif class_age <= 1:
        print(f'Сначала нужно окончить {class_age} год школы!')
    else:
        print(f'Сначала нужно окончить {class_age} лет школы!')
else:
    print('Введите правильное значение')