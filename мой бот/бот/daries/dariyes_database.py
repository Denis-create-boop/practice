import sqlite3  


class Dariye:
    
    def __init__(self, data_name):
        self.db = None
        self.cursor = None
        self.data_name = f"./{data_name}_table.db"
        self.darie_name = None
        self.id = 1
    
    
    def create_table(self, darie_name):
        self.tdarie= darie_name
        with sqlite3.connect(self.data_name) as db:
            self.db = db
            self.cursor = db.cursor()
            query = f""" CREATE TABLE IF NOT EXISTS {darie_name}(id INTEGER, header TEXT, date TEXT, text TEXT, image TEXT) """
            self.cursor.execute(query)
            self.db.commit()
    
    
    def get_last_id(self):
        query = """ SELECT MAX(id) FROM ? """
        self.cursor.executemany(query, (self.darie_name,))
        for row in self.cursor:
            self.id = row[0]
        self.id += 1
        
    
    def add_write(self, new_header, new_date, new_write, image=None):
        self.create_table()
        self.get_last_id()
        query = """ INSERT INTO ? (id, header, date, text, image) VALUES(?, ?, ?, ?, ?) """
        insert_payments = [
            (self.id, new_header, new_date, new_write, image)
        ]
        self.cursor.executemany(query, insert_payments)
        self.db.commit()
    
    
    def show_all(self):
        query = """ SELECT header, date, text FROM ? """
        self.cursor.executemany(query, (self.darie_name,))
        list_writes = []
        for row in self.cursor:
            list_writes.append(row)
        
        return list_writes
    
    
    def find_write(self, data=None, name=None):
        pass
    
    
