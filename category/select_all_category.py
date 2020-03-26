# select_all_category.py
# MM 2020 test select

# open DBSelect and choose all category
from db.SELECT import select_db

record = select_db.DBSelect().select("SELECT * FROM T_Category")

print("ALL CATEGORY ===")
# print id and name of category
for row in record:
    print("[id =", row[0], "| name=", row[1], "| description=", row[2])
