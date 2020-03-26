# select_all_category.py
# MM 19 mars 2020
import connectdb
from mysql.connector import Error


class DBSelect:
    def __init__(self):
        # connect to db
        self.DB = connectdb.DatabaseTools()
        # set db cusor
        self.DBCursos = self.DB.db.cursor()

    def selectAllCategory(self):
        try:
            # execute command
            self.DBCursos.execute("SELECT * FROM `T_Category`")
            # get all records
            records = self.DBCursos.fetchall()
            # commit chang
            self.DB.db.commit()
            # close db cursor (je tiens a dire que vous aviez dit que vous ne vouliez p
            self.DBCursos.close()
            # return all record
            return records
        except Error as e:
            print("error", e)