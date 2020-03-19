# select_all_category.py
# MM
import connectdb
from mysql.connector import Error


class DBSelect:
    def __init__(self):
        self.DB = connectdb.DatabaseTools()
        self.DBCursos = self.DB.db.cursor()

    def selectAllCategory(self):
        try:
            self.DBCursos.execute("SELECT * FROM `T_Category`")
            records = self.DBCursos.fetchall()
            self.DB.db.commit()
            self.DBCursos.close()
            return records
        except Error as e:
            print("error", e)