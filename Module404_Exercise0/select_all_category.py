import connect_db
from GET import select_all_category
from INSERT import insert_one_table

print("please input new category !")
newCategory = input("> ")

try:
    objet_etre_connecte = connect_db.DatabaseTools()

    insert_records = insert_one_table.DbInsertOneTable()

    insert_records.insert_one_record_one_table("INSERT INTO `T_Category` (`id_category`, `name`, `description`, `created_at`) VALUES (NULL, %(values_insert)s, '', CURRENT_TIMESTAMP);",
                                               newCategory)

    objet_etre_connecte.close_connection()

except Exception as e:
    print("error" + e)

record = select_all_category.DBSelect().selectAllCategory()

print("ALL CATEGORY ===")

for row in record:
    print("id =", row[0])
    print("name =", row[1])
