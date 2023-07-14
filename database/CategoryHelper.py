from database.Category import *
from database.InitDatabase import *
from sqlite3 import *

class CategoryHelper:

    def __init__(self):
        create_database()

    def insert_category(self,category:Category):
        try:
            con  = connect("tracker.db")
            cur = con.cursor()
            cur.execute("INSERT INTO category(name,expected_budget) VALUES(?,?)", (category.name,category.expected_budget))
            con.commit()
            con.close()
        except Exception as error:
            print(f"Error: {error}")

    def show_all_categories(self):
        try:
            con = connect("tracker.db")
            cur = con.cursor()
            cur.execute("SELECT * from category")
            result = cur.fetchall()
            cur.close()
            return result

        except Exception as error:
            print(f"Error: {error}")
    
    def show_element_by_category_name(self,name):
        try:
            con = connect("tracker.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM category WHERE name = ?",[name])
            result = cur.fetchone()
            cur.close()
            return result

        except Exception as error:
            print(f"Error: {error}")
    
    