from database.CategoryHelper import *
from database.Category import *
from database.ExpenseHelper import *
from database.Expense import *
from datetime import datetime,date
category = Category("Transport",4000)
cat = CategoryHelper()
cat.insert_category(category)
result = cat.show_all_categories()
print(result)

result = cat.show_element_by_category_name("Meals")
print(result)

expense_helper = ExpenseHelper()
expense = Expense("Hola mundo", datetime.now().strftime("%m-%d-%Y"),400,1)
expense_helper.insert_expense(expense)
result = expense_helper.show_all_expenses()
print(result)

