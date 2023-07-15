from tkinter import Frame,Label
class ExpenseTable(Frame):
    def __init__(self,data):
        super().__init__()
        render_data(data)
    
    def render_data(self,data):
        count_row = 0
        for expense in data:
            id_expense = expense[0]
            Label(self,text=id_expense).grid(row=count_row,column=0)
            description = expense[1]
            Label(self,text=description).grid(row=count_row,column=1)
            date = expense[2]
            Label(self,text=date).grid(row=count_row,column=2)
            quantity = expense[3]
            Label(self,text=3).grid(row=count_row,column=3)
            count_row = count_row + 1
