import sqlite3

class EasyQuestions:
    
    def __init__(self):
        self.cursor = None
        self.db = None
        self.id = 1
    
    def create_table(self):
        """Функция для создания базы данных и таблицы в базе данных"""
        with sqlite3.connect('./easy_questions_db.db') as db:
            self.db = db
            self.cursor = db.cursor()
            query = """ CREATE TABLE IF NOT EXISTS easy (id INTEGER, question TEXT, a TEXT, b TEXT, c TEXT, d TEXT, answer TEXT)"""
            self.cursor.execute(query)
            self.db.commit()
            
         
    def get_id(self):
        
        query = """ SELECT MAX(id) FROM easy """   
        self.cursor.execute(query)
        for row in self.cursor:
            self.id = int(row[0])
        
            
            
    def add_question(self, question):
        
        self.get_id()
        query = """ INSERT INTO easy (id, question, a, b, c, d, answer) VALUES(?, ?, ?, ?, ?, ?, ?)"""
        insert_payments = [
            (self.id + 1, question[0], question[1], question[2], question[3], question[4], question[5],)
        ]
        self.cursor.executemany(query, insert_payments)
        self.db.commit()
        
    def get_question(self, id):
        
        query = """ SELECT * FROM easy WHERE id=? """
        self.cursor.execute(query, (id,))
        question = dict()
        for row in self.cursor:
            question["question"] = row[1]
            question["a"] = row[2]
            question["b"] = row[3]
            question["c"] = row[4]
            question["d"] = row[5]
            question["answer"] = row[6]
        return question
            
            
class MediumQuestions:
    
    def __init__(self):
        self.cursor = None
        self.db = None
        self.id = 1
    
    def create_table(self):
        """Функция для создания базы данных и таблицы в базе данных"""
        with sqlite3.connect('./medium_questions_db.db') as db:
            self.db = db
            self.cursor = db.cursor()
            query = """ CREATE TABLE IF NOT EXISTS medium (id INTEGER, question TEXT, a TEXT, b TEXT, c TEXT, d TEXT, answer TEXT)"""
            self.cursor.execute(query)
            self.db.commit()
    
    def get_id(self):
        
        query = """ SELECT MAX(id) FROM medium """   
        self.cursor.execute(query)
        for row in self.cursor:
            self.id = int(row[0])
        
            
    def add_question(self, question):
        
        self.get_id()
        query = """ INSERT INTO medium (id, question, a, b, c, d, answer) VALUES(?, ?, ?, ?, ?, ?, ?)"""
        insert_payments = [
            (self.id + 1, question[0], question[1], question[2], question[3], question[4], question[5],)
        ]
        self.cursor.executemany(query, insert_payments)
        self.db.commit()  
        
    
    def get_question(self, id):
        
        query = """ SELECT * FROM medium WHERE id=? """
        self.cursor.execute(query, (id,))
        question = dict()
        for row in self.cursor:
            question["question"] = row[1]
            question["a"] = row[2]
            question["b"] = row[3]
            question["c"] = row[4]
            question["d"] = row[5]
            question["answer"] = row[6]
        return question
      
              
class HardQuestions:
    
    def __init__(self):
        self.cursor = None
        self.db = None
        self.id = 1
    
    def create_table(self):
        """Функция для создания базы данных и таблицы в базе данных"""
        with sqlite3.connect('./hard_questions_db.db') as db:
            self.db = db
            self.cursor = db.cursor()
            query = """ CREATE TABLE IF NOT EXISTS hard (id INTEGER, question TEXT, a TEXT, b TEXT, c TEXT, d TEXT, answer TEXT)"""
            self.cursor.execute(query)
            self.db.commit()
    
    def get_id(self):
        
        query = """ SELECT MAX(id) FROM hard """   
        self.cursor.execute(query)
        for row in self.cursor:
            self.id = int(row[0])
            
            
    def add_question(self, question):
        
        self.get_id()
        query = """ INSERT INTO hard (id, question, a, b, c, d, answer) VALUES(?, ?, ?, ?, ?, ?, ?)"""
        insert_payments = [
            (self.id + 1, question[0], question[1], question[2], question[3], question[4], question[5],)
        ]
        self.cursor.executemany(query, insert_payments)
        self.db.commit()
        
    
    def get_question(self, id):
        
        query = """ SELECT * FROM hard WHERE id=? """
        self.cursor.execute(query, (id,))
        question = dict()
        for row in self.cursor:
            question["question"] = row[1]
            question["a"] = row[2]
            question["b"] = row[3]
            question["c"] = row[4]
            question["d"] = row[5]
            question["answer"] = row[6]
        return question
    
            
class LegendQuestions:
    
    def __init__(self):
        self.cursor = None
        self.db = None
        self.id = 1
    
    def create_table(self):
        """Функция для создания базы данных и таблицы в базе данных"""
        with sqlite3.connect('./legend_questions_db.db') as db:
            self.db = db
            self.cursor = db.cursor()
            query = """ CREATE TABLE IF NOT EXISTS legend (id INTEGER, question TEXT, a TEXT, b TEXT, c TEXT, d TEXT, answer TEXT)"""
            self.cursor.execute(query)
            self.db.commit()
            
            
    def get_id(self):
        
        query = """ SELECT MAX(id) FROM legend """   
        self.cursor.execute(query)
        for row in self.cursor:
            self.id = int(row[0])
        
            
            
    def add_question(self, question):
        
        self.get_id()
        query = """ INSERT INTO legend (id, question, a, b, c, d, answer) VALUES(?, ?, ?, ?, ?, ?, ?)"""
        insert_payments = [
            (self.id + 1, question[0], question[1], question[2], question[3], question[4], question[5],)
        ]
        self.cursor.executemany(query, insert_payments)
        self.db.commit()
        
        
    def get_question(self, id):
        
        query = """ SELECT * FROM legend WHERE id=? """
        self.cursor.execute(query, (id,))
        question = dict()
        for row in self.cursor:
            question["question"] = row[1]
            question["a"] = row[2]
            question["b"] = row[3]
            question["c"] = row[4]
            question["d"] = row[5]
            question["answer"] = row[6]
        return question