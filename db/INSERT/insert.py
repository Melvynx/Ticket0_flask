# insert.py
# MM 12 mars 2020 objectif is insert some value in database

from db import connect_db


class DbInsertOneTable:

    # define db var
    def __init__(self):
        # Constructeur
        self.db = connect_db.DatabaseTools()

    def insert(self, request, values):
        try:
            # MM 2020 execute request with value
            self.db.cursor.execute(request, values)
            # MM 2020 commit and close connection
            self.db.db.commit()
            self.db.close_connection()
            return True

        except Exception as e:
            # MM 2020 rollback (undo commit) on error
            self.db.db.rollback()
            print("Unknown error occurred", e)
            return False
