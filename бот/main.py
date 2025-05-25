from random import randrange

from users import *
from game import *
from jokes import *
from calculate import *


def hello():
    """Фунция приветствования"""
    
    say_hello = [
        '               Привет, я твой личный мини-бот',
        '               Добропожаловать, я ваш личный помошник',
        '               Привет, я бот помошник',
        '               Здравствуйте, рад вас видеть, я ваш персональный ассистент'
    ]
    
    ind = randrange(0, 4)
    print(say_hello[ind])
    print()
    print(f"""          Выберите комманду:
                            1 - войти
                            2 - зарегестрироваться
                            3 - продолжить как гость""")
    
    answers_dict = {
        1: login,
        2: registration,
        3: main
    }
    answer = check_command(answers_dict.keys())
    answers_dict[answer]()
    



def main():
    """Функция для работы с ботов в ограниченных условиях не входя в аккаунт"""
    hello_message = f"""
                    Вы вошли как гость, вот некоторые функции которые вам доступны:
                        1 - Посмотреть всех пользователей
                        2 - Калькулятор
                        3 - Расскажи анегдот :-)
                        4 - сыграть в викторину"""
    
    print(hello_message)
    print()
    
    answers_dict = {
        1: look_all_users,
        2: calc,
        3: tell_joke,
        4: game
    }
    answer = check_command(answers_dict.keys())

    answers_dict[answer]()
    
    

if __name__ == '__main__':
    hello()