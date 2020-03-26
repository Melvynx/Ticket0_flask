import connect_db
from db.GET import select_all_category
from db.INSERT import insert_one_table

print("please input new category !")
# input a value from console
newCategory = input("> ")

try:
    # connect db
    objet_etre_connecte = connect_db.DatabaseTools()
    # connect to object DBInsert
    insert_records = insert_one_table.DbInsertOneTable()
    # make insert with new value
    insert_records.insert_one_record_one_table("INSERT INTO `T_Category` (`id_category`, `name`, `description`, `created_at`) VALUES (NULL, %(values_insert)s, '', CURRENT_TIMESTAMP);",
                                               newCategory)
    # close connection
    objet_etre_connecte.close_connection()

except Exception as e:
    print("error" + e)

# open DBSelect and choose all category
record = select_all_category.DBSelect().selectAllCategory()

print("ALL CATEGORY ===")
# print id and name of category
for row in record:
    print("id =", row[0])
    print("name =", row[1])
