from database.InitDatabase import *
from datetime import datetime,date
from sqlite3 import *
from database.Expense import *
class ExpenseHelper:
    def __init__(self):
        create_database()
        self.con = connect("tracker.db")
        
    def show_all_expenses(self):
        cur = self.con.cursor()
        cur.execute("SELECT *  from expenses")
        result = cur.fetchall()
        return result

    def show_expenses_by_day(self,day):
        cur = self.con.cursor()
        cur.execute("SELECT *  from expenses where date = ?",[day])
        result = cur.fetchall()
        return result

    def show_expenses_by_month():
        pass
    
    def show_expenses_by_year():
        pass

    def insert_expense(self, expense:Expense):
        cur = self.con.cursor()
        cur.execute("INSERT INTO expenses(description,date,quantity,id_category) VALUES(?,?,?,?)",[expense.description,expense.date,expense.quantity,expense.id_category])
        self.con.commit()
