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
            if not row[0] is None:
                self.id = int(row[0])
        
    
    def add_new_user(self, password=None, login=None, email=None):
        """Функция для добавления новых пользователей в бд"""
        self.create_table()
        self.get_id()
        users = self.get_all_users()
        query = """ INSERT INTO users (id, login, password, email) VALUES (?, ?, ?, ?) """
        insert_payments = [
            (self.id + 1, login, password, email,),
        ]
        
        self.cursor.executemany(query, insert_payments)
        self.db.commit()
        
    
    def get_all_users(self):
        """Функция для показа имен всех пользователей"""
        self.create_table()
        query = """SELECT login FROM users"""
        self.cursor.execute(query)
        users_list = []
        for row in self.cursor:
            users_list.append(row[0])
        return users_list
    
    
    def get_user(self, login=None, email=None):
        """Функция для получения конкретного пользователя"""
        self.create_table()
        query = f"""SELECT * FROM users WHERE login={login} OR email={email}"""
        
        info_about_user = []
        self.cursor.execute(query)
        
        for row in self.cursor:
            info_about_user.append(row[1])
            info_about_user.append(row[2])
            info_about_user.append(row[3])
        return info_about_user
            
        
        
class Messages:
    
    def __init__(self, login):
        
        self.login = login
        self.cursor = None
        self.db = None
        self.id = 1
        
        
    def create_table(self):
        """Функция для создания базы данных и таблицы в базе данных для хранения писем"""
        with sqlite3.connect('./users_messages_db.db') as db:
            self.db = db
            self.cursor = db.cursor()
            query = f""" CREATE TABLE IF NOT EXISTS {self.login}_messages (id INTEGER, incoming_messages TEXT, sended_messages TEXT, last_id INTEGER)"""
            self.cursor.execute(query)
            self.db.commit() 
            
            
    def show_messages(self, messages):
        """Функция для отображения сообщений пользователя"""
        self.create_table()
        messages = []
        query = f"""SELECT id, {messages} FROM {self.login}_messages"""
        self.cursor.execute(query)
        for row in self.cursor:
            messages.append(row)
            
        return messages
            
    def insert_message(self, message, flag=False):
        self.create_table()
        query = f"""INSERT INTO {self.login}_messages (id, incoming_messages, sended_messages, last_id) VALUES (?, ?, ?, ?)"""
        if flag:
            insert_payments = [
                (self.id + 1, None, message, self.id + 1),
            ]
        else:
            insert_payments = [
                (self.id + 1, message, None, self.id + 2),
            ]
            
        self.cursor.executemany(query, insert_payments)
        self.db.commit()


    def get_id(self):
        self.create_table()
        query = f"""SELECT MAX(id) FROM {self.login}_messages"""
        self.cursor.execute(query)
        for row in self.cursor:
            if not row[0] is None:
                self.id = int(row[0])
                
                
    def get_last_id(self):
        self.create_table()
        self.get_id()
        query = f"""SELECT last_id FROM {self.login}_messages"""
        self.cursor.execute(query)
        id_dict = {
            'id': self.id,
            'last_id': self.id
        }
        for row in self.cursor:
            id_dict['last_id'] = row[0]
        
        return id_dict
        