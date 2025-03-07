import sqlite3  

# таблица зарегестрированных пользователей
class Users:
    """Класс для хранения имен пользователей и для добавления новых пользователей"""
    def __init__(self):
        self.db = None
        self.cursor = None
    
    
    def create_table(self):
        """функция для создания таблицы в бд"""
        
        with sqlite3.connect("./users.db") as db:
            self.db = db
            self.cursor = db.cursor()
            query = f""" CREATE TABLE IF NOT EXISTS users(login TEXT, email TEXT, password TEXT, name TEXT) """
            self.cursor.execute(query)
            self.db.commit()
    
    
    def get_all_users(self):
        """функция для выбора всех пользователей из бд"""
        self.create_table()
        query = """ SELECT * FROM users """
        users = []
        self.cursor.execute(query)
        for row in self.cursor:
            users.append({"login": row[0]})
            users.append({"email": row[1]})
            users.append({"password": row[2]})
            users.append({"name": row[3]})
        
        return users
    
    
    def add_new_user(self, new_login, new_email, new_password, new_name):
        """функция для добавления нового пользователя в бд"""
        self.create_table()
        ls = [
            (new_login, new_email, new_password, new_name,),
        ]
        query = """ INSERT INTO users (login, email, password, name) VALUES(?, ?, ?, ?) """
        self.cursor.executemany(query, ls)
        self.db.commit()


    def get_user(self, login=None, email=None):
        """Функция для получения пароля из бд по логину или паролю"""
        self.create_table()
        if email:
            query = """ SELECT password, name FROM users WHERE email=? """
            password = None
            user_name = None
            self.cursor.execute(query, (email,))
        if login:
            query = """ SELECT password, name FROM users WHERE login=? """
            password = None
            user_name = None
            self.cursor.execute(query, (login,))
        for row in self.cursor:
            password = row[0]
            user_name = row[1]
        
        return [password, user_name]
    
    
    def get_logins(self):
        """Функция для получения всех логинов из бд"""
        self.create_table()
        query = """ SELECT login FROM users """
        self.cursor.execute(query)
        users = []
        for row in self.cursor:
            users.append(row[0])
            
        return users
    
    
    def change_mail(self, email):
        pass
    
    
    def change_login(self, login):
        pass
    
    
    def change_password(self, password):
        pass
