import termcolor
import os

os.system('color')

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
        
        
sky_under_the_bot = f"""
    {termcolor.colored("###################################################################################################", "blue")}
    {termcolor.colored("######################################################*", "blue")}{termcolor.colored("&&&&&&", "white")}{termcolor.colored("*#####################################", "blue")}
    {termcolor.colored("#########*", "blue")}{termcolor.colored("&&&&&", "white")}{termcolor.colored("*###################################*", "blue")}{termcolor.colored("&&&&&&&&&&", "white")}{termcolor.colored("*####################################", "blue")}
    {termcolor.colored("#########*", "blue")}{termcolor.colored("&&&&&&&", "white")}{termcolor.colored("*################################*", "blue")}{termcolor.colored("&&&&&&&&&&&&&&&", "white")}{termcolor.colored("*################################", "blue")}
    {termcolor.colored("###########*", "blue")}{termcolor.colored("&&&&", "white")}{termcolor.colored("*##############################*", "blue")}{termcolor.colored("&&&&&&&&&&&&&&&", "white")}{termcolor.colored("*###################################", "blue")}
    {termcolor.colored("################################################*", "blue")}{termcolor.colored("&&&&&&&&&&&&&", "white")}{termcolor.colored("*####################################", "blue")}
    {termcolor.colored("####################################################*", "blue")}{termcolor.colored("&&&&&&", "white")}{termcolor.colored("*#######################*", "blue")}{termcolor.colored("&&&&&&", "white")}{termcolor.colored("*########", "blue")}
    {termcolor.colored("&", "white")}{termcolor.colored("*###############################################################################*", "blue")}{termcolor.colored("&&&&&&", "white")}{termcolor.colored("*##########", "blue")}
    {termcolor.colored("&&", "white")}{termcolor.colored("*##############################################################################*", "blue")}{termcolor.colored("&&&&&", "white")}{termcolor.colored("*###########", "blue")}
                     """
            
   
                    
message_bot_hello = f"""
                                    {termcolor.colored("||", "white")}                          {termcolor.colored("||", "white")}
                                    {termcolor.colored("||", "white")}                          {termcolor.colored("||", "white")}
                                    {termcolor.colored("||", "white")}                          {termcolor.colored("||", "white")}
            {termcolor.colored("|----------------------------------------------------------------------------|", "light_red")}
            {termcolor.colored("|", "light_red")}                                                                            {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}                                                                            {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}                                                                            {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}                                                                            {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}         {termcolor.colored("$$$$$$$$$$$$$", "light_magenta")}                                {termcolor.colored("$$$$$$$$$$$$$", "light_magenta")}         {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}           {termcolor.colored("=== * ===", "blue")}                                    {termcolor.colored("=== * ===", "blue")}           {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}                                                                            {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}                                    {termcolor.colored("||", "cyan")}                                      {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}                                    {termcolor.colored("||", "cyan")}                                      {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}                                    {termcolor.colored("+", "cyan")}                                       {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}                                                                            {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}                                                                            {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}                                                                            {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}                                                                            {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}                   {termcolor.colored("_._._._._._._._._._._._._._._._._._._")}                    {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}                                                                            {termcolor.colored("|", "light_red")}
            {termcolor.colored("|", "light_red")}                                                                            {termcolor.colored("|", "light_red")}
            {termcolor.colored("|----------------------------------------------------------------------------|", "light_red")}
                                   {termcolor.colored("------ WELCOME TO THE BOT ------", "green")}
"""


