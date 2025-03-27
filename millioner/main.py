from easy_level import *


def check():
    while True:
        level = input(colored("Введите номер уровня ==>> ", "light_green"))
        try:
            level = int(level)
            if level in [1, 2, 3, 4]:
                return level
            else:
                print(colored("Введена неверный уровень", "red"))
        except:
            print(colored("Введена неверная команда, пожалуйста введите число", "red"))


def main():
    hello_message = f"""
                                        {colored("Добро пожаловать на игру - 'Кто хочет стать миллионером'", "light_magenta")}
                        {colored("----------------------------------------------------------------------------------------", "light_red")}
                                            
                                            Выберите уровень сложности игры:
                                            
                            {colored("1 - ", "light_blue")}{colored("Легкий", "white")}
                            {colored("2 - ", "light_blue")}{colored("Средний", "white")}
                            {colored("3 - ", "light_blue")}{colored("Тяжелый", "white")}
                            {colored("4 - ", "light_blue")}{colored("Легендарный", "white")}
    """
    print(hello_message)
    print()
    levels = {
        1: "Легкий",
        2: "Средний",
        3: "Тяжелый",
        4: "Легендарный"
    }
    level = check()
    info_message = f"""
                                        {colored(f"Вы выбрали {levels[level]} уровень.", "light_cyan")}
                                        
                    В игре вы будете сохранять несгораемые суммы, так же у вас есть три подсказки:
                    
                {colored("1 - ", "light_blue")}{colored("50 x 50", "white")}
                {colored("2 - ", "light_blue")}{colored("Помощь зала", "white")}
                {colored("3 - ", "light_blue")}{colored("Две попытки", "white")}
    """
    print()
    print(info_message)
    print("Для продолжения нажмите Enter")
    input(colored("==>> ", "light_green"))
    print(colored("                                             Приступим", "red"))
    time.sleep(0.5)
    game(level)

if __name__ == "__main__":
    main()