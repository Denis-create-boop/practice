import termcolor


hello_message = f"""                                               ____________________
                 --------------------------------------------------------------------------------
                |            {termcolor.colored("__________", "light_magenta")}                 |                 {termcolor.colored("___________", "light_magenta")}            |
                |         {termcolor.colored("---^ ", "light_magenta")}       {termcolor.colored("^---", "light_magenta")}              |              {termcolor.colored("---^", "light_magenta")}         {termcolor.colored("^---", "light_magenta")}         |
                 --------------------------------------------------------------------------------

                 {termcolor.colored("---------------------------------------------------------------------------------", "red")}
                {termcolor.colored("|", "red")}            {termcolor.colored("Здравствуйте, добропожаловать в персонального ассистента", "light_cyan")}             {termcolor.colored("|", "red")}
                {termcolor.colored("|", "red")}                                 {termcolor.colored("Веберите опцию:", "light_cyan")}                                 {termcolor.colored("|", "red")}
                {termcolor.colored("|", "red")}                                       {termcolor.colored("||", "light_cyan")}                                        {termcolor.colored("|", "red")}
                {termcolor.colored("|", "red")}                                       {termcolor.colored("\\/", "light_cyan")}                                        {termcolor.colored("|", "red")}
                {termcolor.colored("|_________________________________________________________________________________|", "red")}
                                            
                                            {termcolor.colored("1 - Войти", "white")}
                                            {termcolor.colored("2 - Зарегестрироваться", "white")}
                                            {termcolor.colored("3 - Продолжить как гость", "white")}"""                                                    


message_login = f"""{termcolor.colored("""     
             ___           ___       _____________       ___                 ___                 ______________
            |   |         |   |     |    _________|     |   |               |   |               |    ______    |
            |   |         |   |     |   |               |   |               |   |               |   |      |   |
            |   |         |   |     |   |               |   |               |   |               |   |      |   |
            |   |_________|   |     |   |_________      |   |               |   |               |   |      |   |
            |    _________    |     |    _________|     |   |               |   |               |   |      |   |
            |   |         |   |     |   |               |   |               |   |               |   |      |   |
            |   |         |   |     |   |               |   |               |   |               |   |      |   |
            |   |         |   |     |   |_________      |   |_________      |   |_________      |   |______|   |
            |___|         |___|     |_____________|     |_____________|     |_____________|     |______________|""", "light_cyan")}"""

message_commands = f"""
                    {termcolor.colored("Добро пожаловать, пожалуйста выбери дальнейшее действие которое ты хочешь совершить:", "cyan")}
                                                1 - Посмотреть свой дневник
                                                2 - Добавить новую запись в дневник
                                                3 - Добавить картинку в дневник
                                                4 - Создать новый дневник
                                                5 - Удалить дневник
                                                6 - Пообщатся с ботом
                                                7 - Выйти
                    """