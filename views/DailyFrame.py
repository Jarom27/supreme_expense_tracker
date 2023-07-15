from tkinter import Frame,Label
from views.ExpenseTable import *
class DailyFrame(Frame):
    def __init__(self):
        super().__init__()
        self.heading = Label(self,text = "Expenses from")
        self.heading.pack()
        self.pack()
