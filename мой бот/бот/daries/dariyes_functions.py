
from datetime import date
from daries import dariyes_database
from users.users_db import Users
from users.users_data import termcolor

darie = dariyes_database.Dariye


def create(name):
    new_dariye_name = input(f"{termcolor.colored("Введи название дневника ==>> ", "light_yellow")}")
    table = darie(name)
    table.create_table(darie_name=new_dariye_name)
    new_dariye = Users()
    new_dariye.create_dariye(user_name=name, dariye_name=new_dariye_name)
    
    
def add_new_write(name):
    """Функция для добавлений записей в таблицу"""
    print()
    header = input(termcolor.colored("Введи заголовок для новой записи ==>> ", "light_yellow"))
    print()
    data = str(date.today())
    text = input(termcolor.colored("Введите запись ==>> ", "light_yellow"))
    answer = input(termcolor.colored("Добавить изображение? да/нет ==>> ", "light_yellow"))
    if answer in ["да", "д"]:
        pass
    else:
        table_us = Users()
        table_name = table_us.get_dariye(name)
        table = dariyes_database.Dariye(name)
        table.add_write(table_name, header, data, text)
        print(termcolor.colored("                                       Запись добавлена", "cyan"))

def add_image(name):
    pass


def show_dariye(name):
    """Функция для показа дневника"""
    dariye = Users()
    if_dariye = dariye.get_dariye(user_name=name)

    if if_dariye:
        table = darie(name)
        writes = table.get_all(if_dariye)
 
        if type(writes) is str:
            print(*writes)
        else:
            for el in writes:
                print()
                print(f"""  {termcolor.colored(el[1], "light_blue")}
                                                {termcolor.colored(el[0], "light_green")}
    {termcolor.colored(el[2], "white")}
                      
    {el[3] if el[3] else ''}
                      """)
                

    else:
        pass
    
    
def del_dariye(name):
    """функция для удаления дневника"""
    dariye = Users()
    if_dariye = dariye.get_dariye(user_name=name)
    if if_dariye:
        get_del_dariye = Users()
        del_dariye = get_del_dariye.get_dariye(user_name=name)
        table = darie(name)
        table.delete_dariye(dariye_name=del_dariye)
    else:
        pass
