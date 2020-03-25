# insert_one_table.py
# MM 12 mars 2020  le but est d'insérer des valeurs en MySql dans une seule table

import connectdb


class DbInsertOneTable():

    # Constructeur, à chaque instanciation de cette classe "DbInsertOneTable()" les lignes de code de la méthode "__init__ (self)" sont interprétées.
    def __init__ (self):  # Constructeur
        # OM 2020.01.28 CONNECTION A LA BD
        self.connection_dbc = connectdb.DatabaseTools()
        # Ouvre un curseur, c'est indispensable pour se déplacer dans les champs de la BD.
        self.DBcursor = self.connection_dbc.db.cursor()
        print("Constructeur CLASSE DbInsertOneTable")


    def insert_one_record_one_table(self, requete_insert_mysql, valeurs_a_inserer):
        try:
            # OM 2020.03.11 Execute la requête avec un passage de paramètres
            self.DBcursor.execute(requete_insert_mysql, {'values_insert' : valeurs_a_inserer})
            # OM 2020.03.11 L'instruction suivante est indispensable pour confirmer l'insertion des données (en cas de problèmes : rollback)
            self.connection_dbc.db.commit()
            self.DBcursor.close()
        except pymysql.Error as error:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une ERREUR : %s", error)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.DataError as error1:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une DataError : %s", error1)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.DatabaseError as error2:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une DatabaseError : %s", error2)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.Warning as error3:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une Warning : %s", error3)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.MySQLError as error4:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une MySQLError : %s", error4)
            print("connection_dbc.db.rollback() insertOneRecord")
        except pymysql.IntegrityError as error5:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print(" Il y a une IntegrityError : %s", error5)
            print("connection_dbc.db.rollback() insertOneRecord")
        except:
            # OM 2020.03.11 L'instruction suivante est indispensable pour annuler l'insertion des données (commande opposée : COMMIT)
            self.connection_dbc.db.rollback()
            print("Unknown error occurred")
        finally:
            print("C'est terminé....finally self.DBcursor.close()")
            self.DBcursor.close()