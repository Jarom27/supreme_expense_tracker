import database.InitDatabase
from database.CategoryHelper import * 
from database.Category import *
from database.Expense import *
from database.ExpenseHelper import *
from logic.budget import *
from datetime import datetime
import pytest

cat_helper = CategoryHelper()
expense_helper = ExpenseHelper()

def test_insert_category():
    category = Category("Trasnport",600)
    cat_helper.insert_category(category)
    result = cat_helper.show_all_categories()
    assert result != []

    category2 = Category("Meals",400)
    cat_helper.insert_category(category2)
    result = cat_helper.show_element_by_category_name("Meals")
    assert result == (2,"Meals",400)

def test_insert_expense():
    expense = Expense("Lays in Walmart",datetime.now(),3.2,2)
    expense_helper.insert_expense(expense=expense)
    assert expense_helper.show_expenses_by_day("2023-07-14") != []

def test_difference_between():
    assert differenceBetweenExpectedBudget(2000,3000) == -1000

pytest.main(["-v", "--tb=line", "-rN", __file__])