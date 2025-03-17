from functions import *
      

def main():
    """Главная функция для работы пользователя с базой данных"""
    
    hello_message = f"""
                        {termcolor.colored("Здравствуйте, пожалуйста выберите действия которые вы хотите выполнить:", "light_yellow")}
                        
        1 - Посмотреть информацию о всех сотрудниках компании
        2 - Посмотреть информацию о конкретном сотруднике
        3 - Посмотреть количество сотрудников
        4 - Изменить данные сотрудника
        5 - Добавить нового сотрудника
        6 - Удалить сотрудника
        7 - Выход
    """
    while True:
        print(hello_message)
        print()
        command = check_command([1, 2, 3, 4, 5, 6, 7])
        command_dict = {
            1: show,
            2: show_employe,
            3: show_amount,
            4: change,
            5: add_employe,
            6: delete_employe
        }
        if command == 7:
            break
        
        command_dict[command]()



if __name__ == "__main__":
    main()
    
    



     
        
 
