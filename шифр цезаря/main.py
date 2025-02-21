
# программа шифр цезаря на для русского языка

flag = False

def question():
    """Функция для уточнения действий программы"""
    global flag
    # спрашиваем пользователя какие действия он хочет сделать
    print(f"""Здравствуйте, какие действия вы хотите совершить? 
          1 - Зашифровать
          2 - Разшифровать""")
    print()
    # запускаем цикл с проверками что бы пользователь ввел корректное число
    while True:
        answer = input("Введите номер команды: ")
        try:
            answer = int(answer)
            if answer in [1, 2]:
                break
            else:
                print("Введена неверная команда")
                print()
        except:
            print("Введены некорректные данные, должно быть число")
            print()

    # меняем flag
    if answer == 1:
        flag = True


def code(message, step, operator):
    """Функция для работы со строкой в зависимости от оператора она либо зашифровывает либо 
    разшифровывает сообщение"""
    # формируем строку из элементов
    answer = ""

    # проходимся циклом по всем элементам строки и сдвигаем на шаг
    for i in range(len(message)):
        # записываем номер элемента из таблицы ASCII
        element = eval(f"{ord(message[i])}{operator}{step}")

        if element < 97:
            element = eval(f"122 - ({step} - ({ord(message[i])} - 96))")

        # записываем получившийся элемент
        answer += chr(element)
    # возвращаем получившуюся строку
    for i in range(len(answer)):
        if answer[i] == "D":
            answer = answer[:i] + ' ' + answer[i+1:]

    return answer


def main():
    global flag
    # вызываем функцию опраса
    question()

    # принимаем строку и шаг
    message = input("Введите строку: ")
    step = input("Введите шаг: ")
    # если flag истина то зашифровываем, иначе разшифровываем
    if flag:
        print(code(message, step, "-"))
    else:
        print(code(message, step, "+"))



if __name__ == "__main__":
    main()