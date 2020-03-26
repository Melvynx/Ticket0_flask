from db.DELETE.delete_db import DBDelete

# take number from user
print("Write id of you're table.")
number = input("> ")

# define request
request = "DELETE FROM `T_Category` WHERE `T_Category`.`id_category` = %(id)s"
DBDelete.delete_one_record(request, number)




