import random


flag = False
count = 1


# функция приветствия
def hello():
    """функция для вывода приветствия и задавания вопроса хочет ли пользователь сыграть"""

    print(f"""                    ------- Добропожаловать в числовую угадайку -------
                    Попробуйте отгадать число которое я загадал :-)
                    Не у многих это выходит""")
    
    question = "Сыграем? да/нет"
    print(question)
    # записываем ответ
    answer = input()

    # возвращаем функцию проверки ответа
    return check_answer(question, answer)

# функция проверки ответа
def check_answer(question, answer):
    """функция для обработки ответов пользователя"""

    while True:
        if answer.lower() in ["да", "д"]:
            return True
        elif answer.lower() in ["нет", "не", "н"]:
            return False
        # если пользователь ввел чтото некорректное то снова вызываем функцию проверки по рекурсии
        else:
            print("Не совсем понял что вы имеете в виду :-)")
            print()
            print(question)
            answer = input()
            return check_answer(question, answer)

# функция проверки числа
def check_number(question, number):
    """функция для проверки что пользователь ввел именно число"""
    while True:
        try:
            number = int(number)
            break
        # если ввел не число то вызываем функцию проверки числа по рекурсии
        except:
            print("Некорректные данные, должно быть число")
            print(question)
            answer = input()
            return check_number(question, answer)

    return int(number)

# функция игры
def game(max_number, my_number, user_number, question):
    """функция для проверки угадал пользователь или нет и отображения ему информации"""
    global count, flag

    #вспомогательная функция для вызова функции игры по рекурсии
    def game_again():
        print(question)
        user_number = input()
        user_number = check_number(question, user_number)
        return game(max_number, my_number, user_number, question)

    if 0 < user_number <= max_number:
        if user_number < my_number:
            print("Ваше число меньше моего")
            print()
            count += 1
            return game_again()

        elif user_number > my_number:
            print("Ваше число больше моего")
            print()
            count += 1
            return game_again()
        # если пользователь угадал то меняем значение переменной flag
        else:
            flag = True

    # если пользователь ввел число либо меньше 1 либо больше максимального
    else:
        print("Введено число вне диапазона")
        print()
        return game_again()


def main():
    global count, flag
    while True:
        if hello() == False:
            break

        # максимальное значение
        question = "Введите максимальное число до которого я могу загадывать"
        print(question)
        max_number = input()
        max_number = check_number(question, max_number)

        # загаданное число
        my_number = random.randrange(1, max_number)

        # число пользователя
        question = "Введите ваше число:"
        print(question)
        user_number = input()
        user_number = check_number(question, user_number)

        # запускаем функцию игры
        game(max_number, my_number, user_number, question)

        # переменная для корректного отображения попыток
        write_count = ""
        if 5 <= count <= 19:
            write_count = "попыток"

        elif count % 10 == 1:
            write_count = "попытку"

        elif count % 10 != 1:
            write_count = "попытки"

        # если пользователь угадал
        if flag:
            print(f"Поздровляем вы угадали число за {count} {write_count}")
            print()
            if hello() == False:
                break


if __name__ == "__main__":
    main()