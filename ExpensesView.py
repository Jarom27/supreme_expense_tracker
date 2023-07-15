from tkinter import *
from tkinter.ttk import *
class ExpenseTreeView(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.expense_scroll_bar = Scrollbar(self)
        self.pack()
        self.expense_scroll_bar.pack(side=RIGHT,fill= Y)
        self.tree_expenses = Treeview(self,yscrollcommand=self.expense_scroll_bar,selectmode="extended")
        self.tree_expenses.pack()
        self.expense_scroll_bar.config(command=self.tree_expenses.yview)

class ExpensesView(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("400x600")
        self.protocol("WM_DELETE_WINDOW",self.back_to_menu)
        self.parent = parent
        self.back_button = Button(self,text="Back to menu",command=self.back_to_menu).pack()
        #Method to disappear the main window
        self.parent.withdraw()
        self.expense_view = ExpenseTreeView(self)
    
    def back_to_menu(self):
        self.parent.deiconify()
        self.destroy()