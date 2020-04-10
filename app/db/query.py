import mysql.connector

from app.db.connect_db import Database

# fetch for return an Object ("one") or an Array of Object ("all")
# sql: string sql (utils/sql_requests), values: obj, fetch: False, "one", "all"
def query(sql, values=False, fetch=False):
  database = Database()
  cursor = database.cursor
  result = []
  try:
    # MM 2020 execute request with value
    if values:
      cursor.execute(sql, values)
    else:
      cursor.execute(sql)

    if fetch == "one":
      result = cursor.fetchone()
    elif fetch == "all":
      result = cursor.fetchall()
    else:
      result = True

    # MM 2020 commit and close connection
    database.db.commit()

  except (Exception, mysql.connector.Error, mysql.connector.InternalError, TypeError) as e:
    # MM 2020 rollback (undo commit) on error
    database.db.rollback()
    print("Unknown error occurred : ", e)
    result = False

  finally:
    database.close_connection()

  return result
