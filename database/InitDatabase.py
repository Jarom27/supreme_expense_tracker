import sqlite3
def create_database():
    try:
        connection  = sqlite3.connect("tracker.db")
        cur = connection.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS category(id_category INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, expected_budget INTEGER)")
        cur.execute("CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY AUTOINCREMENT,description TEXT,date DATE, quantity Integer, id_category INTEGER, FOREIGN KEY(id_category) REFERENCES category(id_category))")
        connection.close()
        
    except ConnectionError as error:
        print(error)
        pass

