import images
from daries import dariyes_functions, dariyes_database
    
def main():

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
    |____________________________________________________________________________________________________________|"""                                                    
    
    print(hello_message)
    print(f"     {images.termcolor.colored("Введите команду:", "light_blue")}")
    command = input(" ==>> ")
    dariye = ["1", "создать", "новый", "личный", "создай"]
    commands = {
        dariyes_functions.create: dariye,
    }
    if command in dariye:
        for k, v in commands.items():
            if v == dariye:
                k(dariyes_database.Dariye)
                break
                


if __name__ == "__main__":
    main()