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
    
    def add_image(self, new_image, header=None, date=None):
        """Функция для добавления изображения"""
        self.set_param()
        if header:
            query = f""" UPDATE {self.data_name} SET image=? WHERE header=? """
            self.cursor.execute(query, (new_image, header))
        elif date:
            query = f""" UPDATE {self.data_name} SET image=? WHERE date=? """
            self.cursor.execute(query, (new_image, date))
        self.db.commit()
        
    def get_date_or_header(self, name, date=None, header=None):
        """Функция для получения либо даты записи либо ее заголовка"""
        self.set_param()
        result = []
        if date:
            query = f""" SELECT date FROM {name} """
            self.cursor.execute(query)
            
        elif header:
            query = f""" SELECT header FROM {self.data_name} """
            self.cursor.execute(query)
            
        for row in self.cursor:
            result.append(row[0])
        
        return result
    
    def delete_dariye(self, dariye_name):
        pass

