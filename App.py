from tkinter import *
from ExpensesView import *
class App(Frame):
    def __init__(self,root):
        super().__init__(root)
        self.parent = root
        self.config(width=200)
        self.show_view_budget_button = Button(self, text="Show Budget", command = self.show_view_budget, width=30)
        self.show_insert_expense_view_button = Button(self, text="Insert new expense", command=self.show_insert_expense_view, width=30)
        self.show_expenses_view_button = Button(self,text = "Show Expenses", command=self.show_view_expenses, width=30)
        self.show_view_budget_button.pack()
        self.show_insert_expense_view_button.pack()
        self.show_expenses_view_button.pack()
        self.place(relx=0.5,rely=0.5,anchor=CENTER)

    def show_view_expenses(self):
        ExpensesView(self.parent)
    def show_insert_expense_view(self):
        pass
    def show_view_budget(self):
        pass

def main():
    root = Tk()
    root.geometry("400x600")
    root.title("Supreme Expense Tracker")
    root.config(bg="#0d0221")
    app = App(root)
    app.mainloop()



if __name__ == "__main__":
    main()
