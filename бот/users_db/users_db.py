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
        query = """SELECT * FROM users WHERE login=? OR email=?"""
        
        info_about_user = []
        self.cursor.execute(query, (login, email))
        
        for row in self.cursor:
            info_about_user.append(row[1])
            info_about_user.append(row[2])
            info_about_user.append(row[3])
        return info_about_user
            
        
        
class Incoming_Messages:
    
    def __init__(self, login):
        
        self.login = str(login) + '_incoming_messages'
        self.cursor = None
        self.db = None
        self.id = 0
        
        
    def create_table(self):
        """Функция для создания базы данных и таблицы в базе данных для хранения  входящих писем"""
        with sqlite3.connect('./users_messages_db.db') as db:
            self.db = db
            self.cursor = db.cursor()
            query = f""" CREATE TABLE IF NOT EXISTS {self.login} (id INTEGER, message TEXT, from_who TEXT, flag TEXT)"""
            self.cursor.execute(query)
            self.db.commit() 
            
            
    def insert_message(self, message, user_login=None):
        """Функция для записи новых сообщений"""
        self.create_table()
        self.get_id()
        query = f"""INSERT INTO {self.login} (id, message, from_who, flag) VALUES (?, ?, ?, ?)"""
        
        insert_payments = [
            (self.id + 1, message, user_login, 'not_read'),
        ]
           
        self.cursor.executemany(query, insert_payments)
        self.db.commit()


    def get_id(self):
        self.create_table()
        query = f"""SELECT MAX(id) FROM {self.login}"""
        self.cursor.execute(query)
        for row in self.cursor:
            if not row[0] is None:
                self.id = int(row[0])
                
                
    def get_not_read_messages(self):
        """Функция для просмотра непрочитанных сообщений"""
        self.create_table()
        query = """SELECT * FROM {} WHERE flag='not_read'""".format(self.login)
        self.cursor.execute(query)
        messages = dict()
        count = 1
        for row in self.cursor:
            messages[count] = row
            count += 1
        return messages
    
    
    def set_flag(self, id):
        """Функция для отметки что сообщение прочитано"""
        query = """UPDATE {} SET flag='read' WHERE id={}""".format(self.login, id)
        self.cursor.execute(query)
        self.db.commit()
        

