from database.InitDatabase import *
from sqlite3 import *
class ExpenseHelper:
    def __init__():
        create_database()
        
    def show_all_expenses():
        con = connect("tracker.db")
        cur = con.cursor()
        cur.execute("SELECT *  from expenses")
        result = cur.fetchall()
        return result

    def show_expenses_by_day():
        pass

    def show_expenses_by_month():
        pass
    
    def show_expenses_by_year():
        pass
