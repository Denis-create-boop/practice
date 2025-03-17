import sqlite3


class Employee:
    """Класс для хранения и изменения информации о сотрудниках работающих в компании"""
    
    def __init__(self):
        self.db = None
        self.cursor = None
        self.id = 1
        self.amount = 1
    
    
    def create_table(self):
        """Функция для создания базы данных и таблицы в базе данных"""
        with sqlite3.connect('./employees_db.db') as db:
            self.db = db
            self.cursor = db.cursor()
            query = """ CREATE TABLE IF NOT EXISTS employees (id INTEGER, name TEXT, first_name TEXT, possition TEXT, salary INTEGER, address TEXT, phone INTEGER, date TEXT, amount INTEGER)"""
            self.cursor.execute(query)
            self.db.commit()    
            
            
    def show_all_employees(self):
        """Функция для отображения всех сотрудников компании"""
        query = """ SELECT * FROM employees """
        self.cursor.execute(query)
        ls_employees = []
        for row in self.cursor:
            ls_employees.append(row)
            
        return ls_employees
    
    
    def show_employee_info(self, id=None, name=None, first_name=None):
        """Функция для отображения информации о конкретном сотруднике"""
        if id:
            query = """ SELECT * FROM employees WHERE id=? """
            self.cursor.execute(query, (id,))
        else:
            query = """ SELECT * FROM employees WHERE name=? AND first_name=? """
            self.cursor.execute(query, (name, first_name,))
            
        for row in self.cursor:
            return row
        
    
    def add_new_employee(self, name, first_name, possition, salary, date, address=None, phone=None):
        """Функция для добавления нового сотрудника в базу данных"""
        self.get_id()
        self.get_amount()
        query = """ INSERT INTO employees (id, name, first_name, possition, salary, address, phone, date, amount) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?) """
        insert_payments = [
            (self.id, name, first_name, possition, salary, address, phone, date, self.amount + 1)
        ]
        self.cursor.executemany(query, insert_payments)
        self.db.commit()
        
    
    def get_id(self):
        """Функция для получения последнего id в таблице """
        query = """ SELECT MAX(id) FROM employees """
        self.cursor.execute(query)

        for row in self.cursor:
            if not row[0] is None:
                self.id = int(row[0]) + 1
                
    
    def get_amount(self):
        """Функция для получения количества сотрудников в компании"""
        query = """ SELECT MAX(amount) FROM employees """
        self.cursor.execute(query)
        
        for row in self.cursor:
            if not row[0] is None:
                self.amount = int(row[0])
                
    
    def change_address(self, address, id=None, name=None, first_name=None):
        """Функция для изменения адреса сотрудника"""
        if id:
            query = """ UPDATE employees SET address=? WHERE id=? """
            insert_payments = [
                (address, id,)
            ]
            self.cursor.executemany(query, insert_payments)
        else:
            query = """ UPDATE employees SET address=? WHERE name=? AND first_name=? """
            insert_payments = [
                (address, name, first_name,)
            ]
            self.cursor.executemany(query, insert_payments)
        self.db.commit()
    
    
    def change_phone(self, new_phone, id=None, name=None, first_name=None):
        """Функция для изменения телефона сотрудника"""
        if id:
            query = """ UPDATE employees SET phone=? WHERE id=? """
            insert_payments = [
                (new_phone, id)
            ]
            self.cursor.executemany(query, insert_payments)
        else:
            query = """ UPDATE employees SET phone=? WHERE name=? AND first_name=? """
            insert_payments = [
                (new_phone, name, first_name,)
            ]
            self.cursor.executemany(query, insert_payments)
        self.db.commit()
    
    
    def change_possition(self, new_possition, id=None, name=None, first_name=None):
        """Функция для изменения должности сотрудника"""
        if id:
            query = """ UPDATE employees SET possition=? WHERE id=? """
            insert_payments = [
                (new_possition, id)
            ]
            self.cursor.executemany(query, insert_payments)
        else:
            query = """ UPDATE employees SET possition=? WHERE name=? AND first_name=? """
            insert_payments = [
                (new_possition, name, first_name,)
            ]
            self.cursor.executemany(query, insert_payments)
        self.db.commit()
    
    
    def change_salary(self, new_salary, id=None, name=None, first_name=None):
        """Функция для изменения зарплаты сотрудника"""
        if id:
            query = """ UPDATE employees SET salary=? WHERE id=? """
            insert_payments = [
                (new_salary, id)
            ]
            self.cursor.executemany(query, insert_payments)
        else:
            query = """ UPDATE employees SET salary=? WHERE name=? AND first_name=? """
            insert_payments = [
                (new_salary, name, first_name,)
            ]
            self.cursor.executemany(query, insert_payments)
        self.db.commit()
    
    
    def del_emloyee(self, id=None):
        """Функция для удаления сотрудника из базы данных"""
        
        query = """ DELETE FROM employees WHERE id=? """
        self.cursor.execute(query, (id,))

        self.get_amount()
        self.get_id()
        self.id -= 1
        self.amount -= 2
        
        query = """ UPDATE employees SET amount=? WHERE id=? """
        self.cursor.execute(query, (self.amount, self.id,))
        self.db.commit()
    


