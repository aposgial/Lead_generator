import sqlite3
#from settings import * #TODO fix the path

class SQLite:
    def __init__(self, file:str="leads.db") -> None:
        self.file = file

    def __enter__(self):
        self.connect = sqlite3.connect(self.file)
        return self.connect.cursor()

    def __exit__(self, type, value, traceback):
        if self.connect:
            self.connect.commit()
            self.connect.close()
            