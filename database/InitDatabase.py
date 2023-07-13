import sqlite3
def create_database():
    try:
        connection  = sqlite3.connect("tracker.db")
        cur = connection.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS categoria(id_categoria PRIMARY KEY, name TEXT, expected_budget INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY,description TEXT,date DATE, id_categoria INTEGER, FOREIGN KEY(id_categoria) REFERENCES categoria(id_categoria))")
        
    except ConnectionError as error:
        print(error)
        pass

