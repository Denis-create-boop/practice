import keyboard
import termcolor
import re as r
from users import users_db

IS_LOGIN =False

# маска пароля
def masked_input(prompt):
    """Функция для замены вводимого пароля на символ *"""
    secret_symbol = "*"
    print(prompt, end='', flush=True)
    input_str = ""
    
    while True:
        event = keyboard.read_event(suppress=True)
        key = event.name
        
        if event.event_type == 'down':
            if key == "enter":
                print()
                break
            elif key == 'backspace' and len(input_str) > 0:
                input_str = input_str[:-1]
                print('\b \b', end='', flush=True)
                
            elif len(key) == 1:
                print(secret_symbol, end='', flush=True)
                input_str += key
    return input_str


def check_password(again=False, login=False):
    """Функция для проверки корректности пароля"""
    upper_letters = False
    lower_letters = False
    numbers = False
    while True:
        if again:
            password = masked_input(termcolor.colored("Введите пароль еще раз ==>> ", "light_yellow"))
        else:
            password = masked_input(termcolor.colored("Введи пароль ==>> ", "light_yellow"))
        for el in password:
            try:
                el = int(el)
                numbers = True
            except:
                if el == el.upper():
                    upper_letters = True
                elif el == el.lower():
                    lower_letters = True
        if len(password) >= 6:        
            if upper_letters and lower_letters and numbers:
                break
            else:
                if login:
                    break
                else:
                    print()
                    print(termcolor.colored("           Пожалуйста введите корректный пароль, в пароле должны быть загланые буквы, строчные буквы а также цифры", "red"))
                    print()
        else:
            if login:
                break
            else:
                print()
                print(termcolor.colored("           Слишком короткий пароль введите не менее 6 символов", "red"))
                print()
    return password


def check_login(register=False):
    """Функция для проверки логина"""
    if register:
        user = users_db.Users()
        logins = user.get_logins()
        return logins
        
    else:
        
        login = input(termcolor.colored("Введите ваш логин или имейл ==>> ", "light_yellow"))
        users = users_db.Users()
        if "@" in login:
            data = users.get_user(email=login)
        else:
            data = users.get_user(login=login)

        return data


def login_to_db():
    global iS_LOGIN
    """функция для входа в систему"""
    print(termcolor.colored("                       Хорошо введите данные ниже:", "light_green"))
    print()
    while True:
        
        login = check_login()
        password = check_password(login=True)
        if login[0] == password:
            print(termcolor.colored(f"                                                  Добро пожаловать {login[1]}", "light_cyan"))
            print()
            iS_LOGIN = True
            break
        else:
            print(termcolor.colored("               Введен неверный логин (почта) или пароль", "red"))
    return login[1]


def register_new_user():
    """Функция регистрации нового пользователя"""

    while True:
        name = input(termcolor.colored("Введите ваше имя ==>> ", "light_yellow"))
        if not name is None and len(name) > 2:
            break
        else:
            print()
            print(termcolor.colored("                   Слишком короткое имя", "red"))
            print()
            
    while True:
        login = input(termcolor.colored("Введите ваш логин ==>> ", "light_yellow"))
        login_in_db = check_login(register=True)
        if login not in login_in_db:
            break
        else:
            print()
            print(termcolor.colored("                   Такой логин уже зарегестрирован", "red"))
            print()
            
    while True:
        email = input(termcolor.colored("Введите имейл (необязательно) ==>> ", "light_yellow"))
        pattern = r"\b[A-Za-z0-9_.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not email or r.search(pattern, email):
            break
        else:
            print()
            print(termcolor.colored("                       Неверный формат имейл", "red"))
            print()
    
    while True:
        password = check_password()
        password_again = check_password(again=True)   
        if password == password_again:
            break
        else:
            print()
            print(termcolor.colored("           Неверный повторный пароль попробуйте снова", "red"))
            print()
    print(termcolor.colored(f"{name} Вы успешно зарегестрировались и вошли в аккаунт", "magenta"))
    table = users_db.Users()
    table.add_new_user(login, email, password, name)
    return name