from .db_context_manager import SQLite

class Model():
    def __init__(self) -> None:
        self.create_table_searches()
        self.create_table_places()
        self.create_table_types()
        self.create_table_operating_hours()
        self.create_table_reviews()
        self.create_table_suggestions()


    def create_table_searches(self):
        query = '''CREATE TABLE IF NOT EXISTS searches
                    (lead_id INTEGER PRIMARY KEY autoincrement,
                    location_searched TEXT,
                    type_searched TEXT,
                    result_sum INTEGER,
                    date_searched DATE,
                    suggestions BOOLEAN
                );
                '''
        with SQLite() as cursor:
            cursor.execute(query)

    def create_table_places(self):
        query = '''CREATE TABLE IF NOT EXISTS places
                    (result_id INTEGER PRIMARY KEY autoincrement,
                    lead_id INTEGER,
                    place_id TEXT,
                    name TEXT,
                    address TEXT,
                    phone TEXT,
                    maps_url TEXT,
                    rating REAL,
                    total_ratings INTEGER,
                    FOREIGN KEY (lead_id) REFERENCES searches(lead_id)
                );
                '''
        with SQLite() as cursor:
            cursor.execute(query)

    def create_table_types(self):
        query = '''CREATE TABLE IF NOT EXISTS types
                    (result_id INTEGER,
                    type TEXT,
                    FOREIGN KEY (result_id) REFERENCES places(result_id)
                );
                '''
        with SQLite() as cursor:
            cursor.execute(query)

    def create_table_operating_hours(self):
        query = '''CREATE TABLE IF NOT EXISTS operating_hours
                    (result_id INTEGER,
                    day TEXT,
                    status TEXT,
                    opening_time TEXT,
                    closing_time TEXT,
                    FOREIGN KEY (result_id) REFERENCES places(result_id)
                );
                '''
        with SQLite() as cursor:
            cursor.execute(query)

    def create_table_reviews(self):
        query = '''CREATE TABLE IF NOT EXISTS reviews
                    (result_id INTEGER,
                    author_name TEXT,
                    rate INTEGER,
                    language TEXT,
                    text TEXT,
                    FOREIGN KEY (result_id) REFERENCES places(result_id)
                );
                '''
        with SQLite() as cursor:
            cursor.execute(query)

    def create_table_suggestions(self):
        query = '''CREATE TABLE IF NOT EXISTS suggestions
                    (result_id INTEGER,
                    suggestion TEXT,
                    FOREIGN KEY (result_id) REFERENCES places(result_id)
                );
                '''
        with SQLite() as cursor:
            cursor.execute(query)


    def insert_searches(self, search_data:dict):
        query = '''INSERT INTO searches
                    (location_searched, 
                    type_searched, 
                    result_sum, 
                    date_searched, 
                    suggestions)
                    VALUES (?, ?, ?, ?, ?);
                '''
        with SQLite() as cursor:
            cursor.execute(query, tuple(search_data.values()))
            
    def insert_places(self, place_data:dict):
        query = '''INSERT INTO places 
                    (lead_id,
                    place_id,
                    name,
                    address,
                    phone,
                    maps_url,
                    rating,
                    total_ratings)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
                '''
        with SQLite() as cursor:
            cursor.execute(query, tuple(place_data.values()))

    def insert_types(self, type_date:dict):
        query = '''INSERT INTO types 
                    (result_id,
                    type)
                    VALUES (?, ?);
                '''
        with SQLite() as cursor:
            cursor.execute(query, tuple(type_date.values()))
    
    def insert_operating_hours(self, operating_hours_data:dict):
        query = '''INSERT INTO operating_hours 
                    (result_id,
                    day,
                    status,
                    opening_time,
                    closing_time)
                    VALUES (?, ?, ?, ?, ?);
                '''
        with SQLite() as cursor:
            cursor.execute(query, tuple(operating_hours_data.values()))

    def insert_reviews(self, review_data:dict):
        query = '''INSERT INTO reviews 
                    (result_id,
                    author_name,
                    rate,
                    language,
                    text)
                    VALUES (?, ?, ?, ?, ?);
                '''
        with SQLite() as cursor:
            cursor.execute(query, tuple(review_data.values()))
    
    def insert_suggestions(self, suggestion_data:dict):
        query = '''INSERT INTO suggestions 
                    (result_id,
                    suggestion)
                    VALUES (?, ?);
                '''
        with SQLite() as cursor:
            cursor.execute(query, tuple(suggestion_data.values()))

    
    def select_searches(self):
        query = '''SELECT * FROM searches'''

        with SQLite() as cursor:
            data = cursor.execute(query)
            return data.fetchall()

    def select_places(self, lead_id):
        query = '''SELECT * FROM places WHERE lead_id=?'''
        
        with SQLite() as cursor:
            data = cursor.execute(query, (lead_id,))
            return data.fetchall()
        
    def select_types(self, result_id):
        query = '''SELECT * FROM types WHERE result_id=?'''
        
        with SQLite() as cursor:
            data = cursor.execute(query, (result_id,))
            return data.fetchall()
        
    def select_operating_hours(self, result_id):
        query = '''SELECT * FROM operating_hours WHERE result_id=?'''
        
        with SQLite() as cursor:
            data = cursor.execute(query, (result_id,))
            return data.fetchall()

    def select_reviews(self, result_id):
        query = '''SELECT * FROM reviews WHERE result_id=?'''
        
        with SQLite() as cursor:
            data = cursor.execute(query, (result_id,))
            return data.fetchall()
        
    def select_suggestions(self, result_id):
        query = '''SELECT * FROM suggestions WHERE result_id=?'''
        
        with SQLite() as cursor:
            data = cursor.execute(query, (result_id,))
            return data.fetchall()
        


from datetime import date            
m = Model()
search_data = {
    'location_searched': 'volos',
    'type_searched': 'bar',
    'result_sum': 200,
    'date_searched': date.today(),
    'suggestions': False
    }

#m.insert(search_data)