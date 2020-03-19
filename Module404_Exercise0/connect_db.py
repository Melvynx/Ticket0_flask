# connect_db.py
# MM 12 mars 2020 Connexion bd

import mysql.connector


# OM 2020.03.16 Se connecter à la BD.
class DatabaseTools():
    def __init__(self):
        print("Constructeur classe DatabaseTools ")

    def connect_ma_bd(self):
        # set db condig
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
        print("db connect impec")

        return self

    # OM 2020.03.11 Petite méthode pour fermer la connection à la BD
    def close_connection(self):
        if self.connect_ma_bd().db:
            print("Dans la méthode close_connection et la BD est FERMEE")
            self.db.close()
        else:
            print("Dans la méthode close_connection et y'a rien a fermer")
