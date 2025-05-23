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
    pass


def look_all_users():
    users = Users.get_all_users()
    for user in users:
        print("==> ", user)


def profile(user):
    pass