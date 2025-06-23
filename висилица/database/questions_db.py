import sqlite3


class Categories:
    """Класс для хранения категорий слов"""
    
    def __init__(self):
        """Инициализатор"""
        self.cursor = None
        self.db = None
        
    
    def create_table(self):
        """функция для создания таблицы в базе данных"""
        with sqlite3.connect('./висилица/database/databases/category.db') as db:
            self.db = db
            self.cursor = db.cursor()
            query = """ CREATE TABLE IF NOT EXISTS categories (category TEXT)"""
            self.cursor.execute(query)
            self.db.commit()   
    
    
    def show_categories(self):
        """функция для вывода всех имеющихся категорий"""
        self.create_table()
        query = """SELECT * FROM categories"""
        categories = []
        self.cursor.execute(query)
        for row in self.cursor:
            categories.append(row[0])
            
        return categories

    def add_category(self, category):
        """функция для добавления категорий в таблицу"""
        self.create_table()
        categories = self.show_categories()
        if category not in categories:
            query = """INSERT INTO categories (category) VALUES (?)"""
            self.cursor.execute(query, (category,))
            self.db.commit()
            return True
        else:
            return False
    
    
    def delete_category(self, category):
        """функция для удаления категории из таблицы"""
        self.create_table()
        categories = self.show_categories()
        if category in categories:
            query = """DELETE FROM category WHERE category = ?"""
            self.cursor.execute(query, (category, ))
            self.db.commit()
            return True
        else:
            return False
    
    
class Words:
    """Класс для хранения слов"""
    global Categories
    def __init__(self):
        """Инициализатор"""
        self.categories = Categories().show_categories()
        self.db = None
        self.cursor = None
        
    
    def create_table(self):
        """функция для создания таблицы"""
        with sqlite3.connect('./висилица/database/databases/words.db') as db:
            self.db = db
            self.cursor = db.cursor()
            query = """ CREATE TABLE IF NOT EXISTS words (category TEXT, word TEXT)"""
            self.cursor.execute(query)
            self.db.commit()
    
    
    def add_word(self, category, word):
        """функция для добавления слов в таблицу"""
        self.create_table()
        words = self.show_words(category=category)
        
        if word not in words and category in self.categories:
            query = """INSERT INTO words (category, word) VALUES (?, ?)"""
            self.cursor.execute(query, (category, word,))
            self.db.commit()
            return True
        else:
            return (category, self.categories)
    
    
    def del_word(self, category, word):
        """функция для удаления слов из таблицы"""
        self.create_table()
        words = self.show_words()
        if word in words:
            query = """DELETE FROM words WHERE word = ? AND category = ?"""
            self.cursor.executemany(query, (word, category,))
            self.db.commit()
            return True
        else:
            return False
    
    
    def show_words(self, category):
        """функция для вывода всех имеющихся слов в определенной категории"""
        self.create_table()
        query = """SELECT * FROM words WHERE category = ?"""
        all_words = []
        self.cursor.execute(query, (category, ))
        for row in self.cursor:
            all_words.append(row[1])
            
        return all_words
    

w = Words()
