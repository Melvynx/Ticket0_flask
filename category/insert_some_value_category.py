# insert_some_value_category.py
# MM 2020 test insert some value

from db.INSERT import insert_one_table

print("please input name for a new category !")
# input a value from console
name = input("> ")
print("Now pleas write a description !")
description = input("> ")

try:
    # define var for insert
    db_insert = insert_one_table.DbInsertOneTable()
    # define var for request and values
    request = "INSERT INTO `T_Category` (`id_category`, `name`, `description`, `created_at`) VALUES (NULL, %(name)s, %(description)s, CURRENT_TIMESTAMP);"
    values = {"name": name, "description": description}
    # insert on db
    db_insert.insert(request, values)

except Exception as e:
    print("error" + e)
