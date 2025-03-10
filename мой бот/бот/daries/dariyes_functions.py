
from datetime import date
from daries import dariyes_database
from images import my_images
import re as r
from users.users_db import Users
from users.users_data import termcolor

darie = dariyes_database.Dariye


def create(name):
    new_dariye_name = input(f"{termcolor.colored("Введи название дневника ==>> ", "light_yellow")}")
    table = darie(name)
    table.create_table(darie_name=new_dariye_name)
    new_dariye = Users()
    new_dariye.create_dariye(user_name=name, dariye_name=new_dariye_name)
    print(termcolor.colored("Дневник создан успешно", "light_green"))
    
def check_image_number():
    """функция для проверки правильного выбора изображения"""
    while True:
        print(f"""  {termcolor.colored("Выбери изображение, введи номер изображения для выбора. Чтобы посмотреть изображение введи 'посмотреть' и номер изображения через пробел:", "green")}
        1 - heart""")
        answer = input("Введи команду ==>> ")
        if len(answer.split()) > 1 and answer.split()[0].lower() == 'посмотреть':
            my_images[int(answer.split()[1])]()
            print()
        else:
            try:
                answer = int(answer)
                if answer in my_images.keys():
                    image = answer
                    break
                else:
                    print(termcolor.colored("Введен неверный номер изображения", "red"))
                    print()
            except:
                print(termcolor.colored("Введены некорректные данные, должно быть число", "red"))
                print()
    return image
    
    
def check_writes(name):
    data = None
    header = None
    table = dariyes_database.Dariye(name)
    table_name = Users().get_dariye(name)
    answer = input(termcolor.colored("Введите заголовок или дату в формате (ГГГГ-ММ-ДД) записи куда хотите добавить изображение ==>> "))
    pattern = r'\d{4}-\d{2}-\d{2}'
    if r.search(pattern, answer):
        data = answer
        ls_date = table.get_date_or_header(table_name, date=data)
        if data in ls_date:
            return True
        else:
            return False
    else:
        header = answer
        ls_header = table.get_date_or_header(table_name, header=header)
        if header in ls_header:
            return True
        else:
            return False
    
    
def add_new_write(name):
    """Функция для добавлений записей в таблицу"""
    table = Users()
    dariye = table.get_dariye(name)
    if not dariye is None:
        print()
        header = input(termcolor.colored("Введи заголовок для новой записи ==>> ", "light_yellow"))
        print()
        data = str(date.today())
        text = input(termcolor.colored("Введите запись ==>> ", "light_yellow"))
        image = input(termcolor.colored("Добавить изображение? да/нет ==>> ", "light_yellow"))
        if image in ["да", "д"]:
            image = check_image_number()
            table_us = Users()
            table_name = table_us.get_dariye(name)
            table = dariyes_database.Dariye(name)
            table.add_write(table_name, header, data, text, image=image)
            print(termcolor.colored("                                       Запись добавлена", "cyan"))
        else:
            table_us = Users()
            table_name = table_us.get_dariye(name)
            table = dariyes_database.Dariye(name)
            table.add_write(table_name, header, data, text)
            print(termcolor.colored("                                       Запись добавлена", "cyan"))
    else:
        print(termcolor.colored("Что бы добавить запись в дневник сначала создайте дневник", "light_red"))

def add_image(name):
    table = Users()
    dariye = table.get_dariye(name)
    if dariye:
        new_image = check_image_number()
        flag = check_writes(name)
        if flag:
            print("ok")
        else:
            print("no")
    


def show_dariye(name):
    """Функция для показа дневника"""
    global my_images
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
                print(f"""      {termcolor.colored(el[1], "light_blue")}
                      
                                                {termcolor.colored(el[0], "light_green")}
                                                
    {termcolor.colored(el[2], "white")}
    {my_images[el[3]]() if el[3] else ''}
                      """)
                print()
                

    else:
        print(termcolor.colored("У вас пока нет дневника", "light_red"))
    
    
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
        print(termcolor.colored("У вас пока нет дневника", "light_red"))
