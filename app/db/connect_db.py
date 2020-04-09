# connect_db.py
# MM 12 mars 2020 connect bd

import mysql.connector


# OM 2020.03.16 Se connecter à la BD.
class Database:
  def __init__(self):
    # set db condig
    try:
      config = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'port': 8889,
        'database': 'melvyn_malherbe_tiqet_bd_104',
        'raise_on_warnings': True,
      }
      # connect db
      self.db = mysql.connector.connect(**config)
      self.cursor = self.db.cursor(dictionary=True)
      print("db connect impec")

    except mysql.connector.Error:
      print("Something went wrong.")

  # MM 2020 close db connection
  def close_connection(self):
    if self.db:
      self.cursor.close()
      self.db.close()
    else:
      print("Error, db alredy close.")
