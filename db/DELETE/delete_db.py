# delete_db
# MM 2020 delete one record one my database

from db import connect_db


class DBDelete:

    def __init__(self):
        # Database connect
        self.db = connect_db.DatabaseTools()

    def delete_one_record(self, request, id_record):
        try:
            # execute request with id
            self.db.cursor.execute(request, {"id": id_record})

            self.db.db.commit()
            # Database close connection
            self.db.close_connection()

        except Exception as e:
            print("delete doesn't work", e)
            self.db.db.rollback()
