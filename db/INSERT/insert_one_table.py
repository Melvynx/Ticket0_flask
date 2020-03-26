# insert_one_table.py
# MM 12 mars 2020  le but est d'insérer des valeurs en MySql dans une seule table

from db import connect_db


class DbInsertOneTable():

    # define db var
    def __init__(self):  # Constructeur
        self.db = connect_db.DatabaseTools()

    def insert(self, request, values):
        try:
            # MM 2020 execute request with value
            self.db.cursor.execute(request, values)
            # MM 2020 commit and close connection
            self.db.db.commit()
            self.db.close_connection()
        except:
            # MM 2020 rollback (undo commit) on error
            self.db.db.rollback()
            print("Unknown error occurred")
