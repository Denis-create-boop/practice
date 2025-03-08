
from daries import dariyes_functions, dariyes_database
from messages import *
from users import users_data
import time
    
is_login = False
name = None


def check_command(ls_commands):
    """Функция для проверки правильности ввода команд"""
    command = None
    st_command = ""
    for com in ls_commands:
        st_command += str(com)
        st_command += " или "
    while True:
        print(f"                    {termcolor.colored("Введите команду:", "light_blue")}")
        command = input("==>> ")
        try:
            command = int(command)
            if command not in ls_commands:
                print(termcolor.colored(f"      Введена неверная команда, пожалуйста выберите {st_command[:-5]}", "red"))
                print()
            else:
                break
        except:
            print(termcolor.colored("       Введены неверные данные, пожалуйста введите число", "red"))
            print()
    return command


def main():
    global is_login, name, write
    print()
    
    
    while True:
        if is_login:
            
            print(message_login)
            time.sleep(1)
            print()
            print(termcolor.colored("           ------------------------------------------------------------------------------------------------------", "red"))
            time.sleep(1)
            print(message_commands, flush=True)
            command = check_command([1, 2, 3, 4, 5, 6, 7])
            command_do_it = {
                1: dariyes_functions.show_dariye,
                2: dariyes_functions.add_new_write,
                3: dariyes_functions.add_image,
                4: dariyes_functions.create,
                5: dariyes_functions.del_dariye,
                6: "",
                7: goodbye()
            }
            command_do_it[command](name)
        
        else:
            print(hello_message)
            command = check_command([1, 2, 3])
            if command == 1:
                name = users_data.login_to_db()
                is_login = True
            elif command == 2:
                name = users_data.register_new_user()
                is_login = True
            else:
                pass
            


def goodbye():
    pass

if __name__ == "__main__":
    main()