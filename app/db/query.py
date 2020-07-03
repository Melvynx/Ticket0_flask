import mysql.connector

from app.db.connect_db import Database

# fetch for return an Object ("one") or an Array of Object ("all")
# sql: string sql (utils/sql_requests), values: obj, fetch: False, "one", "all"
def query(sql, values=False, fetch=False, multi=False):
    database = Database()
    # MM 2020 if  database connection crashed, we directly return false
    if not database.is_connect:
        print("Error : Database connection crashed.")
        return False

    try:
        cursor = database.cursor
        result = []
        # MM 2020 execute request with value
        if values:
            cursor.execute(sql, values, multi=multi)
        else:
            cursor.execute(sql, multi=multi)

        if fetch == "one":
            result = cursor.fetchone()
        elif fetch == "all":
            result = cursor.fetchall()
        else:
            result = True

        database.db.commit()

    except (
        Exception,
        AttributeError,
        TypeError,
        mysql.connector.Error,
        mysql.connector.InternalError,
        mysql.connector.DatabaseError,
    ) as e:
        # MM 2020 rollback (undo commit) on error
        database.db.rollback()
        print("[query] error occurred : ", e)
        result = False

    finally:
        database.close_connection()

    return result
