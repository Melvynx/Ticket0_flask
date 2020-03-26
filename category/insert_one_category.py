# insert_one_category.py
# MM 2020 test insert one value

from db.INSERT import insert_one_table

print("please input new category !")
# input a value from console
newCategory = input("> ")

try:
    db_insert = insert_one_table.DbInsertOneTable()
    # make insert with new value
    request = "INSERT INTO `T_Category` (`id_category`, `name`, `description`, `created_at`) VALUES (NULL, " \
              "%(values_insert)s, '', CURRENT_TIMESTAMP);"
    db_insert.insert(request, {"values_insert": newCategory})

except Exception as e:
    print("error", e)
