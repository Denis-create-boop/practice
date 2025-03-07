import images
from daries import dariyes_functions, dariyes_database
    
is_login = False

def main():
    global is_login
    print()
    print("                                                   ____________________")
    print(f"""                     --------------------------------------------------------------------------------
                    |            {images.termcolor.colored("__________", "light_magenta")}                  |             {images.termcolor.colored("___________", "light_magenta")}               |
                    |         {images.termcolor.colored("---^ ", "light_magenta")}       {images.termcolor.colored("^---", "light_magenta")}               |          {images.termcolor.colored("---^", "light_magenta")}         {images.termcolor.colored("^---", "light_magenta")}            |
                     --------------------------------------------------------------------------------""")
   
    hello_message = f"""     ____________________________________________________________________________________________________________
    |          {images.termcolor.colored("Здравствуйте я бот помошник, меня зовут Роб, вот несколько функций которые я умею:", "green")}                |
    |                                                                                                            |
    |   1 - Могу создать ваш личный дневник и хранить его в тайне                                                |
    |   2 - Могу рассказать анегдот                                                                              |
    |   3 - Могу нарисовать вам картинку                                                                         |
    |   4 - Могу показать вам ваш личный дневник                                                                 |
    |   5 - Могу изменить либо добавить запись в ваш дневник                                                     |
    |   6 - Войти                                                                                                |
    |   7 - Зарегестрироваться                                                                                   |
    |____________________________________________________________________________________________________________|"""                                                    
    
    while True:
        if is_login:
            print("hello")
            break
        
        else:
            print(hello_message)
            command = dariyes_functions.check_command([1, 2, 3, 4, 5])
            dariye = [1, "создать", "новый", "личный", "создай"]
            commands = {
                dariyes_functions.create: dariye,
            }
            print()
            do_command = None
            if command in dariye:
                do_command = dariye

            for key, value in commands.items():
                if value == do_command:
                    is_login = key(dariyes_database)
                    break


if __name__ == "__main__":
    main()