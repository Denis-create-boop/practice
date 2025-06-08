from users_db.users_db import Users, Incoming_Messages
import time
from jokes import *
from game import *
from calculate import *




def login():
    """Функция для входа в личный кабинет"""
    print("         Введите ваш логин или имейл:")
    answer = input("==>> ")
    user = Users().get_user(login=answer, email=answer)
    print()
    print("         Введите пароль:")
    password = input("==>> ")
    if user:
        if user[1] == password:
            profile(user)
        else:
            print("Неверный логин или пароль")
            login()
    else:
        print("Неверный логин или пароль")
        login()


def registration():
    """Функция для регистрации нового пользователя"""
    
    Login = check_login()
    logins = Users().get_all_users()
    if Login not in logins:
        Password = check_password()
        Email = check_email()
        users = Users()
        users.add_new_user(password=Password, login=Login, email=Email)
        profile([Login, Password, Email])
        
    else:
        print(" Такой логин уже занят введите пожалуйста другой")
        registration()


def look_all_users():
    users = Users().get_all_users()
    for user in users:
        print("==> ", user)


def profile(user):
    print("                                 Добро пожаловать", user[0])
    print()
    message = Incoming_Messages(user[0])
    messages = message.get_not_read_messages()
    if len(messages) > 0:
        
        print(f'''      У вас есть новые сообщения
              1 - Прочитать
              2 - Продолжить''')
        answer = check_command([1, 2])
        if answer == 1:
            print(messages)
            for k, v in messages.items():
            
                print(f"""                                    Сообщение:
    {v[1]}
    
                                    От:
    {v[2]}
    """)  
            
                message.set_flag(v[0])
                print()
                print("""    1 - Ответить
    ENTER ==>> Следующее""")
                
                answer = check_command([1], flag=True)
                if answer == 1:
                    send_message(user, user_login=v[2])
            print("         Больше сообщений нет")
            time.sleep(0.1)
            print()

    print(f"""      Выберите действие:
            1 - Сыграть в викторину
            2 - Расскажи анегдот
            3 - Мои сообщения
            4 - Написать другому пользователю
            5 - Калькулятор
            6 - Выход""")
    answer = check_command([1, 2, 3, 4, 5, 6])
    command_dict = {
        1: game,
        2: tell_joke,
        3: my_messages,
        4: send_message,
        5: calc,
        6: exit,
    }
    
    command_dict[answer](user[0])


def check_login(flag=False):
    """Функция для проверки корректности логина"""
    login = ''
    users = Users()
    all_users = users.get_all_users()
    if flag:
        print("         Введите логин пользователя которому хотите написать")
        login = input('==>> ')
        if login in all_users:
            pass
        else:
            return False
    
    else:
        while True:
            print("         Введите логин")
            login = input("==>> ")
            if len(login) < 4:
                print("Логин слишком короткий")
            else:
                try:
                    login = int(login)
                    print("Логин не должен состоять только из цыфр")
                except:

                    if login in all_users:
                        print("     Такой логин уже зарегестрирован")
                    else:
                        break
        return login
    
    
def check_password():
    """Функция для проверки валидности пароля"""
    flag_lower_letter = False
    flag_upper_letter = False
    flag_sym = False
    flag_integer = False
    
    while True:
        print("Введите пароль")
        password_1 = input("==>> ")
        print("Введите пароль повторно")
        password_2 = input("==>> ")
        if password_1 == password_2:
            for i in password_1:
                try:
                    i = int(i)
                    flag_integer = True
                except:
                    if i in ".,-=)(?!":
                        flag_sym = True
                    else:
                        if i == i.lower():
                            flag_lower_letter = True
                        else:
                            flag_upper_letter = True
            if flag_upper_letter and flag_lower_letter and flag_integer and flag_sym:
                return password_1
            else:
                print("Введен неккоректный пароль, пароль должен иметь заглавные буквы, строчные буквы, цифры и символы")
        else:
            print("Вы ввели разные пароли")
            
            
def check_email():
    """Функция для проверки валидности имейла"""
    while True:
        print("Введите имейл")
        email = input("==>> ")
        if '@' in email:
            if len(email[:email.index('@')]) > 4 and len(email[email.index('@') + 1:]) > 4 and ('.ru' in email[email.index('@') + 2:] or '.com' in email[email.index('@') + 2:]):
                return email
            else:
                print("Введен неккоректный имейл")
        else:
            print("Введен неккоректный имейл")
            
def check_command(commands, flag=False):
    """Функция для проверки команды"""
    answer = input("Введите команду ==>> ")
    if flag:
        if answer == '':
            return
    else:
        try:
            answer = int(answer)
            if answer in commands:
                return answer
            else:
                print("Введена некорректная команда")
                check_command(commands)
        except:
            print("Введены некорректные данные, должно быть число")
            check_command(commands)
        return



def my_messages(my_login=None):
    pass


def send_message(user, user_login=None):
    if user_login is None:
        print("                 Введите логин пользователя которому хотите написать")
        login_other_user = input('==>> ')
        users = Users()
        all_users = users.get_all_users()
        if login_other_user in all_users:
            print("                     Введите ваше сообщение")
            message = input("==>> ")
            users_message = Incoming_Messages(login_other_user)
            users_message.insert_message(message, user_login=user)
            
        else:
            print("Введен неверный логин")
            send_message(user)
    else:
        print("                     Введите ваше сообщение")
        message = input("==>> ")
        users_message = Incoming_Messages(user_login)
        users_message.insert_message(message, user_login=user)
        
    
    profile(user)
    
def exit(user):
    print("Всего доброго", user)