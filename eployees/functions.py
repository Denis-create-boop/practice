from employees_db import Employee
import datetime
import termcolor
import re


table = Employee()
table.create_table()


def check_command(ls_command):
    """Функция для проверки корректности введения команд"""

    while True:
        command = input(termcolor.colored("Введите команду ==>> ", "light_green"))
        try:
            command = int(command)
 
            if command in ls_command:
                return command
            else:
                print(termcolor.colored("               Введена неверная команда", "red"))
                print()
        except:
            print(termcolor.colored("                   Введенны некорректные данные, должно быть число", "red"))
            print()


def check_correct_answer():
    
    def check_employe(id=None, name=None, first_name=None):
        if id:
            result = table.show_employee_info(id=id)
        if name and first_name:
            result = table.show_employee_info(name=name, first_name=first_name)
        if result:
            return result

        else:
            return None

    while True:
        message = termcolor.colored("                       Пожалуйста введите id или имя и фамилию сотрудника через пробел:", "light_cyan")
        print(message)
        print()
        answer = input(termcolor.colored("==>> ", "light_green"))
        if len(answer.split()) > 1:
            employe = check_employe(name=answer.split()[0], first_name=answer.split()[1])
            return employe
        elif len(answer.split()) <= 1:
            try:
                answer = int(answer)
                employe = check_employe(id=answer)
                return employe
                
            except:
                print(termcolor.colored("                   Введены некорректные данные", "red"))
                print()
                
                
def check_phone(employee):
    while True:
        new_phone = input(termcolor.colored("Введите новый телефон ==>> ", "light_green"))
        phone = re.split(r'[- ,.]+', new_phone)
        phone = ''.join(phone)
        if phone[0] == '+':
            phone = phone[1:]

        if len(phone) < 11:
            print(termcolor.colored("Введен некорректный номер телефона", "red"))
        else:
            try:
                phone = int(phone)
                table.change_phone(new_phone=phone)
                print(termcolor.colored(f"Телефон сотрудника {employee[1]} {employee[2]} успешно изменен", "green"))
                break
            except:
                print(termcolor.colored("Введен некорректный номер телефона", "red"))
  
  
def check_salarry():
    while True:
        new_salary = input(termcolor.colored("Введите новую зарплату ==>> ", "light_green"))
        try:
            new_salary = int(new_salary)
            return new_salary
        except:
            print(termcolor.colored("Неверный формат данных, должно быть число", "red"))
                
def show():
    """Функция для выведения все сотрудников"""
    global table
    employes = table.show_all_employees()
    if employes:
        for row in employes:
            print(f"""
    id: {row[0]}
    Дата принятия на работу: {row[7]}
    Имя: {row[1]}
    Фамилия: {row[2]}
    Должность: {row[3]}
    Зарплата: {row[4]}
    Адрес: {row[5]}
    Телефон: {row[6]}
              """)
            print()
    else:
        print(termcolor.colored("                       База данных пока пуста", "light_magenta"))
        
              
def show_employe():
    """Функция для отображения информации о конкретном сотруднике"""
    employe = check_correct_answer()
                
    if employe:
            print(f"""
    id: {employe[0]}
    Дата принятия на работу: {employe[7]}
    Имя: {employe[1]}
    Фамилия: {employe[2]}
    Должность: {employe[3]}
    Зарплата: {employe[4]}
    Адрес: {employe[5]}
    Телефон: {employe[6]} 
                """)

    else:
        print(termcolor.colored("                       Такого сотрудника нет в базе данных", "red"))   
        
        
def change():
    message = f"""
                        {termcolor.colored("Пожалуйста выберите действия которые вы хотите выполнить:", "light_yellow")}
        
        1 - Изменить адрес сотрудника
        2 - Изменить номер телефрна сотрудника
        3 - Изменить должность сотрудника
        4 - Изменить зарплату сотрудника
    """
    print(message)
    print()
    command = check_command([1, 2, 3, 4])
    command_dict = {
        1: change_address,
        2: change_phone,
        3: change_possition,
        4: change_salary,
    }
    command_dict[command]()


def show_amount():
    table.get_amount()
    result = table.amount
    print(f"{termcolor.colored("Количество сотрудников в компании: ", "light_green")}{result}")
    
    
def add_employe():
    print(termcolor.colored("                   Пожалуйста введите данные ниже:", "light_magenta"))
    while True:
        name = input(termcolor.colored("Введите имя нового сотрудника ==>> ", "light_green"))
        if len(name) > 1:
            break
        else:
            print(termcolor.colored("                   Имя должно состоять больше чем из одного элемента", "red"))
            
    while True:
        first_name = input(termcolor.colored("Введите фамилию нового сотрудника ==>> ", "light_green"))
        if len(first_name) > 1:
            break
        else:
            print(termcolor.colored("                   Фамилия должна состоять больше чем из одного элемента", "red"))
    
    while True:
        possition = input(termcolor.colored("Введите должность нового сотрудника ==>> ", "light_green"))
        if len(possition) > 1:
            break
        else:
            print(termcolor.colored("                   должность должна состоять больше чем из одного элемента", "red"))
    
    while True:
        salary = input(termcolor.colored("Введите зарплату нового сотрудника ==>> ", "light_green"))
        try:
            salary = int(salary)
            break
        except:
            print(termcolor.colored("                   Введены некорректные данные, введите число", "red"))
            
    address = input(termcolor.colored("Введите адресс нового сотрудника / не обязательно ==>> ", "light_green"))
    phone = None
    
    while True:
        phone = input(termcolor.colored("Введите телефон нового сотрудника / не обязательно ==>> ", "light_green"))
        if phone:
            try:
                phone = int(phone)
                break
            except:
                print(termcolor.colored("                   Введены некорректные данные, пожалуйста введите номер без пробелов и дополнительных символов", "red"))
        else:
            break
        
    data = datetime.datetime.now()
    
    table.add_new_employee(name, first_name, possition, salary, data, address=address, phone=phone)   
    print(termcolor.colored("                       Сотрудник добавлен", "light_magenta"))
    
    
def change_address():
    result = check_correct_answer()
    if result:
        new_address = input(termcolor.colored("Введите новый адрес ==>> ", "light_green"))
        table.change_address(address=new_address)
        print(termcolor.colored(f"Адресс сотрудника: {result[1]} {result[2]} успешно изменен", "green"))
    
    else:
        print(termcolor.colored("                       Такого сотрудника нет в базе данных", "red")) 


def change_phone():
    result = check_correct_answer()
    if result:
        check_phone(result)
        #table.change_phone(new_phone=new_phone)
        print(termcolor.colored(f"Тедефон сотрудника: {result[1]} {result[2]} успешно изменен", "green"))
    else:
        print(termcolor.colored("                       Такого сотрудника нет в базе данных", "red")) 


def change_possition():
    result = check_correct_answer()
    if result:
        new_possition = input(termcolor.colored("Введите новую должность ==>> ", "light_green"))
        table.change_possition(new_possition=new_possition)
        print(termcolor.colored(f"Должность сотрудника: {result[1]} {result[2]} успешно изменена", "green"))
    else:
        print(termcolor.colored("                       Такого сотрудника нет в базе данных", "red")) 


def change_salary():
    result = check_correct_answer()
    if result:
        new_salary = check_salarry()
        table.change_salary(new_salary=new_salary)
        print(termcolor.colored(f"Зарплата сотрудника: {result[1]} {result[2]} успешно изменена", "green"))
    else:
        print(termcolor.colored("                       Такого сотрудника нет в базе данных", "red")) 


def delete_employe():
    employee = check_correct_answer()
    if employee:
        table.del_emloyee(id=employee[0])
        print(termcolor.colored(f"                         Сотрудник: {employee[1]} {employee[2]} успешно удален", "light_green"))
    
    else:
        print(termcolor.colored("                       Такого сотрудника нет в базе данных", "red"))