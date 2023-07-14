class Category:
    def __init__(self, name,expected_budget):
        self.name = name
        self.expected_budget = expected_budget

    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return f"{self.name};{self.expected_budget}"