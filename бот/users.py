from my_db.my_db import Users



def login():
    """Функция для входа в личный кабинет"""
    print("         Введите ваш логин или имейл:")
    answer = input("==>> ")
    user = Users.get_user(login=answer, email=answer)
    print()
    print("         Введите пароль:")
    password = input("==>> ")
    if user:
        if user[2] == password:
            profile(user)
        else:
            print("Неверный логин или пароль")
            login()
    else:
        print("Неверный логин или пароль")
        login()


def registration():
    """Функция для регистрации нового пользователя"""
    
    login = check_login()
    password = check_password()
    email = check_email()
    print(login)
    print(password)
    print(email)
    


def look_all_users():
    users = Users.get_all_users()
    for user in users:
        print("==> ", user)


def profile(user):
    pass


def check_login():
    """Функция для проверки корректности логина"""
    login = ''
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