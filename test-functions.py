import database.InitDatabase
from database.CategoryHelper import * 
from database.Category import *
from logic.budget import *
import pytest

cat_helper = CategoryHelper()

def test_insert_category():
    category = Category("Trasnport",600)
    cat_helper.insert_category(category)
    result = cat_helper.show_all_categories()
    assert result != []

    category2 = Category("Meals",400)
    cat_helper.insert_category(category2)
    result = cat_helper.show_element_by_category_name("Meals")
    assert result == ["Meals",400]

    

def test_difference_between():
    assert differenceBetweenExpectedBudget(2000,3000) == -1000

pytest.main(["-v", "--tb=line", "-rN", __file__])