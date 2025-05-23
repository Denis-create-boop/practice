import sqlite3

class Users:
    """Класс для хранения и изменения информации о пользователях"""
    
    def __init__(self):
        self.id = 1
        self.db = None
        self.cursor = None
    
    
    def create_table(self):
        """Функция для создания базы данных и таблицы в базе данных"""
        with sqlite3.connect('./users_db.db') as db:
            self.db = db
            self.cursor = db.cursor()
            query = """ CREATE TABLE IF NOT EXISTS users (id INTEGER, login TEXT, password TEXT, email TEXT)"""
            self.cursor.execute(query)
            self.db.commit() 
            
            
    def get_id(self):
        """Функция для получения последнего id из таблицы"""
        self.create_table()
        query = """SELECT MAX(id) FROM users"""
        self.cursor.execute(query)
        for row in self.cursor:
            if row:
                self.id = int(row[0])
        
    
    def add_new_user(self, password, login=None, email=None):
        """Функция для добавления новых пользователей в бд"""
        self.create_table(self)
        self.get_id(self)
        query = """INSERT INTO users (id, login, password, email) VALUES ?, ?, ?, ?"""
        insert_payments = [
            (self.id, login, password, email,)
        ]
        self.cursor.executemany(query, insert_payments)
        self.db.commit()
        
    
    def get_all_users(self):
        """Функция для показа имен всех пользователей"""
        self.create_table(self)
        query = """SELECT login FROM users"""
        self.cursor.execute(query)
        users_list = []
        for row in self.cursor:
            users_list.append(row[0])
        return users_list
    
    
    def get_user(self, login=None, email=None):
        """Функция для получения конкретного пользователя"""
        self.create_table(self)
        query = """SELECT * FROM users WHERE login=? OR email=?"""
        insert_payments = [
            (login, email,)
        ]
        info_about_user = []
        self.cursor.executemany(query, insert_payments)
        
        for row in self.cursor:
            info_about_user.append(row[0])
            
        