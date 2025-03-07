from datetime import date
from users import users_data
from users.users_data import termcolor




def check_command(ls_commands):
    """Функция для проверки правильности ввода команд"""
    command = None
    st_command = ""
    for com in ls_commands:
        st_command += str(com)
        st_command += " или "
    while True:
        print(f"     {termcolor.colored("Введите команду:", "light_blue")}")
        command = input("==>> ")
        try:
            command = int(command)
            if command not in ls_commands:
                print(termcolor.colored(f"Введена неверная команда, пожалуйста выберите {st_command[:-5]}", "red"))
                print()
            else:
                break
        except:
            print(termcolor.colored("Введены неверные данные, пожалуйста введите число", "red"))
            print()
    return command


def create(db):

    print(f"""                              {termcolor.colored("Отлично давай создадим твой личный дневник :)", "magenta")}
                        {termcolor.colored("Чтобы создать дневник тебе нужно войти либо зарегестрироваться", "magenta")}
                                {termcolor.colored("------------------------------------------", "magenta")}
                                        {termcolor.colored("Выбери дальнейшее действие:", "white")}
                                        1 - войти
                                        2 - зарегестрироваться
                                {termcolor.colored("------------------------------------------", "magenta")}""")
    
    command = check_command([1, 2])
    if command == 1:
        users_data.login_to_db()
        return True
        
    else:
        users_data.register_new_user()
    
    # darie_name = input(f"{termcolor.colored("Введи название дневника ==>> ", "light_yellow")}")
    # table = db.Dariye(darie_name)
    # table.create_table(darie_name)
    # print(termcolor.colored("Твой дневник успешно создан, теперь ты можешь добавлять в него записи", "magenta"))
    
    
    

