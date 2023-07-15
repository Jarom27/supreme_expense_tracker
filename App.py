from tkinter import *
from tkinter import ttk
from views.DailyFrame import DailyFrame

class App(Frame):
    def __init__(self,root):
        super().__init__(root)
        self.notebook = ttk.Notebook(self)
        self.daily_frame = DailyFrame()
        self.notebook.add(self.daily_frame,text = "Daily", padding = 20)
        self.notebook.pack(padx=10,pady=10)
        self.pack()

def main():
    root = Tk()
    root.title("Supreme Expense Tracker")
    root.geometry("400x600")
    app = App(root)
    app.mainloop()


if __name__ == "__main__":
    main()