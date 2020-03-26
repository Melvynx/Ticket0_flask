# insert_one_table.py
# MM 12 mars 2020  le but est d'insérer des valeurs en MySql dans une seule table

from db import connect_db


class DbInsertOneTable():

    # Constructeur, à chaque instanciation de cette classe "DbInsertOneTable()" les lignes de code de la méthode "__init__ (self)" sont interprétées.
    def __init__ (self):  # Constructeur
        self.db = connect_db.DatabaseTools()


    def insert(self, request, values):
        try:
            # MM 2020 execute request with value
            self.db.cursor.execute(request, values)
            # OM 2020.03.11 L'instruction suivante est indispensable pour confirmer l'insertion des données (en cas de problèmes : rollback)
            self.db.db.commit()
            self.db.close_connection()
        except:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.db.db.rollback()
            print("Unknown error occurred")
        finally:
            print("C'est terminé....finally self.DBcursor.close()")
