from termcolor import colored
from random import choice, randrange
import time


FIFTY_FIFTY = True
HELP_PEOPLE = True
TWO_ANSWERS = True


total_win = 0


def get_list_id(max_id):
    ls = []
    while len(ls) < 11:
        id = randrange(1, max_id)
        if id not in ls:
            ls.append(id)
            
    return ls

def game(level):
    questions_table = f"""
                                {colored("Вас ждет 15 вопросов за каждый правильный ответ вы получаете деньги", "light_blue")}
                        {colored("Ознакомтесь с таблицей вопросов и выплат, желтый цвет это несгораемые суммы:", "light_blue")}
                        
                                                1 - 1000
                                                2 - 2000
                                                {colored("3 - 5000", "light_yellow")}
                                                4 - 10 000
                                                5 - 20 000
                                                6 - 50 000
                                                {colored("7 - 100 000", "light_yellow")}
                                                8 - 200 000
                                                9 - 250 000
                                                {colored("10 - 500 000", "light_yellow")}
                                                11 - 550 000
                                                12 - 600 000
                                                {colored("13 - 700 000", "light_yellow")}
                                                14 - 800 000
                                                15 - 1 000 000
    """
    print(questions_table)
    print(colored("         Для начала игры нажмите Enter", "light_red"))
    input(colored("==>> ", "light_green"))
    if level == 1:
        from questions import EasyQuestions
        table = EasyQuestions()
        table.create_table()
        table.get_id()
        max_id = table.id
        id_list = get_list_id(max_id)
        
    elif level == 2:
        pass
    elif level == 3:
        pass
    elif level == 4:
        pass