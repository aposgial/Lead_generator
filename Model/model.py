from db_context_manager import SQLite

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


    def insert(self, search_data):
        query = '''INSERT INTO searches
                    (location_searched, 
                        type_searched, 
                        result_sum, 
                        date_searched, 
                        suggestions
                    )VALUES (?, ?, ?, ?, ?);
                    '''
        with SQLite() as cursor:
            cursor.execute(query, (
                                search_data['location_searched'],
                                search_data['type_searched'],
                                search_data['result_sum'],
                                search_data['date_searched'],
                                search_data['suggestions']
                                ))
            


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