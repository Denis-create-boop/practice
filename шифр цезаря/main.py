
# программа шифр цезаря для двух языков русского и английского

# глобальные переменные для вывода сообщений и определения того зашифровываем мы или разштфровываем
flag = False
error = None
message = None

# глобальные константы для работы с языком программы и алфавитом
START = None
END = None
LANGUAGE = None

# функция кодировки / разкодировки
def code(message, step):
    """Функция для работы с сообщением пользователя. Кодирует либо декодирует сообщения"""
    global START, END, flag
    operator = "+"
    
    if flag:
        operator = "-"

    # формируем строку из элементов
    answer = ""
    
    # проходимся циклом по всем элементам строки и сдвигаем на шаг
    for i in range(len(message)):
        # записываем номер элемента из таблицы ASCII
        element = eval(f"{ord(message[i])}{operator}{step}")
        
        if element < START:
            element = eval(f"{END} - ({step} - ({ord(message[i])} - {START - 1}))")
        
        if element > END:
            element = eval(f'{element} - {END} + {START - 1}')
            
        # записываем получившийся элемент
        answer += chr(element)
        
    # возвращаем получившуюся строку
    russion = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
    english = 'qwertyuiopasdfghjklzxcvbnm'
    for i in range(len(answer)):
        if answer[i] not in russion and answer[i] not in english:
            answer = answer[:i] + ' ' + answer[i+1:]

    return answer


# функция проверки данных
def check(lan_flag=None, step=None):
    """Функция для проверки ответа пользователя и для вывода исключений если пользователь ввел что-то некорректное"""
    global error, message, flag, LANGUAGE, START, END
    answer = None
    
    if step:
        if LANGUAGE == "Русский":
            message = "Введите шаг"
        elif LANGUAGE == "English":
            message = "Enter step"
            
        
    # заупскаем цикл который будет работаь пока пользователь не введет число
    while True:
        # выводим сообщение
        if not message is None:
            answer = input(f"{message}: ")
        else:
            answer = input("Enter command / Введите команду: ")
        print() 
        try:
            answer = int(answer)
            # проверяем что пользователь ввел нужное число
            if answer not in [1, 2] and not step:
                if LANGUAGE == "English":
                    error = "Icorrect command please enter 1 or 2"
                elif LANGUAGE == "Русский":
                    error = "Неверная команда, пожалуйста введите 1 или 2"
                else:
                    error = "Icorrect command please enter 1 or 2 / Неверная команда, пожалуйста введите 1 или 2"
                print(error)
            else:
                error = None
                if step:
                    return answer  
                break   
        except:
            # проверяем что пользователь ввел нужное число
            if LANGUAGE == "English":
                error = "Incorrect data entered must be a number"
            elif LANGUAGE == "Русский":
                error = "Введены некорректные данные, должно быть число"
            else:
                error = "Incorrect data entered must be a number / Введены некорректные данные, должно быть число"
            print(error)
            

    # проверяем устанавливаем ли мы язык
    if lan_flag:
        # проверяем какой язык устанавливаем
        if answer == 2:
            LANGUAGE = "Русский"
            error = "Введены некорректные данные, должно быть число"
            message = "Введите команду"
            START = 1072
            END = 1103
        elif answer == 1:
            LANGUAGE = "English"
            error = "Incorrect data entered must be a number"
            message = "Enter command" 
            START = 97
            END = 122
    # если не язык то проверяем если пользователь выбрал 1 (зашифровать) то меняем флаг   
    else:
        if answer == 1:
            flag = True
        
            
    
# главная функция программы
def main():
    """Функция для опроса пользователя спрашиваем язык программы и дальнейшие действия"""
    global LANGUAGE, START, END, flag
    
    # сообщение об установке языка программы
    choose_language = f"""choose language please / пожалуйста выберите язык:
    1 - English
    2 - Русский"""
    print(choose_language)
    # вызываем функцию проверки
    check(lan_flag=True)
    
    # если после проверки установился русский то продолжаем на русском
    if LANGUAGE == "Русский":
        # спрашиваем пользователя что он хочет сделать (зашифровать/разшифровать)
        massage = f"""Здравствуйте. Пожалуйста выберите действие которое вы хотите сделать:
        1 - зашифровать сообщение
        2 - разшифровать сообщение"""
        print(massage)
        # вызываем функцию проверки
        check()
        message = "Введите ваше сообщение"
        print(message)
        user_message = input()
        step = check(step=True)
        print(code(user_message, step))
    
    # если после проверки установился английский то продолжаем на английском
    if LANGUAGE == "English":
        # спрашиваем пользователя что он хочет сделать (зашифровать/разшифровать)
        message = f"""Wellcome. Please select the actions you want to do:
        1 - encrypt the message
        2 - descrypt the message"""
        print(message)
        # вызываем функцию проверки
        check()
        message = "Enter your message"
        print(message)
        user_message = input()
        step = check(step=True)
        print(code(user_message, step))
    


if __name__ == "__main__":
    main()