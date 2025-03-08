import sqlite3  


class Dariye:
    
    def __init__(self, data_name):
        self.db = None
        self.cursor = None
        self.data_name = f"./{data_name}_table.db"
        self.darie_name = None
    
    
    def set_param(self):
        with sqlite3.connect(self.data_name) as db:
            self.db = db
            self.cursor = db.cursor()
    
    def create_table(self, darie_name):
        self.set_param()
        new_darie_name = ""
        for i in darie_name:
            if i == " ":
                new_darie_name += "_"
            else:
                new_darie_name += i
                
        query = f""" CREATE TABLE IF NOT EXISTS {new_darie_name}(header TEXT, date TEXT, text TEXT, image TEXT) """
        self.cursor.execute(query)
        self.db.commit()
        
    
    def add_write(self, name, new_header, new_date, new_write, image=None):
        self.set_param()
        query = f""" INSERT INTO {name} (header, date, text, image) VALUES(?, ?, ?, ?) """
        insert_payments = [
            (new_header, new_date, new_write, image)
        ]
        self.cursor.executemany(query, insert_payments)
        self.db.commit()
    
    
    def get_all(self, dariye_name):
        """Функция для получения всех записей дневника"""
        self.set_param()
        query = f""" SELECT * FROM {dariye_name} """
        self.cursor.execute(query)
        all_writes = []
        
        for row in self.cursor:
            all_writes.append(row)
            
        if all_writes:
            return all_writes
        
        else:
            return "В дневнике пока нет записей"
    
    
    def find_write(self, data=None, name=None):
        pass
    
    
    
    def delete_dariye(self, dariye_name):
        pass

