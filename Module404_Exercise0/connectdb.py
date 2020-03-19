# connectdb.py
# MM 2020.20.20

import pymysql
import pymysql.connections
import mysql.connector


class DatabaseTools:

    def __init__(self):
        # Set config
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': 8889,
            'database': 'melvyn_malherbe_tiqet_bd_104',
            'raise_on_warnings': True,
        }

        self.db = mysql.connector.connect(**config)

        print("db connect impec")

    def close_connection(self):
        if self.db:
            print("La bd vient d'être fermée.")
            self.db.close()
        else:
            print("Il n'y a rien a fermer.")
