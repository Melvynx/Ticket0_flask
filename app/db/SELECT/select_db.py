# select_db.py
# MM 19 mars 2020 select from database

from mysql.connector import Error

from app.db import connect_db


class DBSelect:
    def __init__(self):
        # connect to db
        self.db = connect_db.DatabaseTools()
        # set db cusor

    def select(self, request, values=False):
        try:
            # execute command
            if values:
                self.db.cursor.execute(request, values)
            else:
                self.db.cursor.execute(request)
            # get all records
            records = self.db.cursor.fetchall()
            # close db
            self.db.close_connection()
            # return all record
            return records
        except Error as e:
            print("error", e)
