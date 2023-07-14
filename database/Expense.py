class Expense:
    def __init__(self, description, date, id_category):
        self.description = description
        self.date = date
        self.id_category = id_category

    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return f"{self.description};{self.date};{self.id_category}"