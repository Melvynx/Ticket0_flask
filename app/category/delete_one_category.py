# delete_one_category.py
# MM 2020 test delete one value

from app.db.DELETE.delete_db import DBDelete

# take number from user
print("Write id of you're table.")
number = input("> ")

# define request
request = "DELETE FROM `T_Category` WHERE `T_Category`.`id_category` = %(id)s"

db_delete = DBDelete()

db_delete.delete_one_record(request, number)
