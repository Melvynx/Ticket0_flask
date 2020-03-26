# delete_db
# MM 2020
# delete one record one my database

from db import connect_db


class DBDelete():

    def delete_one_record(request, id_record):
        try:
            #Database connect
            db = connect_db.DatabaseTools()
            #execute request with id
            db.cursor.execute(request, {"id": id_record})

            db.db.commit()
            #Database close connection
            db.close_connection()
        except Exception as e:
            print("delete doesn't work" + e)
            db.db.rollback()
