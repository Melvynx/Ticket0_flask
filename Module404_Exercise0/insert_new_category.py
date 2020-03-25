# insert_new_category.py
# MM 12 mars 2020 essai d'insertion

import connect_db
# Importer le fichier "InsertOneTable" dans lequel il y a quelques classes et méthodes en rapport avec le sujet d'insertion dans UNE SEULE table.
from INSERT import insert_one_table

# OM 202.03.11 Démonstration en classe, juste pour faire un objet "jeveux_etre_connecte"

try:
    objet_etre_connecte = connect_db.DatabaseTools()

    # OM 2020.01.28 Une instance "insert_records" pour permettre l'utilisation des méthodes de la classe DbInsertOneTable
    insert_records = insert_one_table.DbInsertOneTable()

    val = "new "
    print(val)


    # insert_records.insert_one_record_one_table("INSERT IGNORE INTO t_genres (id_genre, intitule_genre) VALUES (null, %(values_insert)s)", val)
    insert_records.insert_one_record_one_table("INSERT INTO `T_Category` (`id_category`, `name`, `description`, `created_at`) VALUES (NULL, %(values_insert)s, '', CURRENT_TIMESTAMP);", val)

    objet_etre_connecte.close_connection()

except Exception as e:
    print("error" + e)
