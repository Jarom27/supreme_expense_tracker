from database.CategoryHelper import *
from database.Category import *

category = Category("Transport",4000)
cat = CategoryHelper()
cat.insert_category(category)
result = cat.show_all_categories()
print(result)

result = cat.show_element_by_category_name("Meals")
print(result)