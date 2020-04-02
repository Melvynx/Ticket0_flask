# 5_flask_afficher_table_genres.py
# OM 2020.03.29 Démonstration de l'utilisation du microframework Flask
# Méthode POST et GET (plus de renseignements ci-dessous)
# https://www.w3schools.com/tags/ref_httpmethods.asp
# Le retour des données se fait grâce à une page en HTML et le langage JINJA
# Avec le traitement de l'erreur 404.
#
# A l'aide de Flask et de MySql, le but est d'afficher tous les lignes de la table "t_genres" en MySql.

# Importer le fichier "select_table.py" dans lequel il y a quelques classes et méthodes en rapport avec l'affichage des données dans UNE SEULE table.
import json

# Importation de la Class Flask
from flask import Flask, render_template, request, redirect, url_for, abort

from DATABASE.SELECT import select_table

# Un objet "obj_mon_application" pour utiliser la classe Flask
# Pour les personnes qui veulent savoir ce que signifie __name__ une démonstration se trouve ici :
# https://www.studytonight.com/python/_name_-as-main-method-in-python
# C'est une chaîne de caractère qui permet de savoir si on exécute le code comme script principal
# appelé directement avec Python et pas importé.
obj_mon_application = Flask(__name__,template_folder='../templates')

# Fonction dir() extraordinaire pour explorer les attributs, les fonctions.
print(dir(obj_mon_application))


#
# Pour traquer l'erreur 404 et ainsi envoyer le fichier "templates/erreur.html"
# On peut ainsi personnaliser l'affichage de l'erreur.
# Pour la suite de votre vie ... en NAIN-formatique https://developer.mozilla.org/fr/docs/Web/HTTP/Status
#
@obj_mon_application.errorhandler(404)
def page_not_found(error):
    # Afficher un message dans la console
    obj_mon_application.logger.info(f"L'URL est fausse... {request.url}")
    return render_template("erreur.html", val_erreur_fichier_html=error), 404

# Une "route" c'est une URL ou des URL(s) qui permet(tent) d'interpréter la fonction au-dessous.
# Dans Flask, les routes sont déclarées via le décorateur @obj_mon_application.route("/")
@obj_mon_application.route("/")
def index():
    # On affiche une chaîne en format HTML, ici des éléments de titre de section de différentes grandeurs
    return "<h1>flask_3_routes_params Le bonheur en 2020</h1><h3>Rester chez soi !<h3><h6>Hello world!</h6>"

# http://127.0.0.1:5002/genres
@obj_mon_application.route('/genres')
def afficher_genres():
    try:
        # OM 2020.03.26 Une instance "select_record" pour permettre l'utilisation des méthodes de la classe DbSelectOneTable
        select_record = select_table.DbSelectOneTable()
        # Pour l'affichage du contenu suite à une requête SELECT avec un tri sur la colonne id_genre
        mysql_select_string = "SELECT * FROM t_genres ORDER BY id_genre ASC"
        # Les résultats de la requête se trouvent dans la variable "records_select" de type <class 'list'>
        records_select = select_record.select_rows(mysql_select_string)

        # Affiche différentes formes de "sortie" des données. Il y en a beaucoup d'autres, suivant l'utilisation finale (client WEB par ex.)
        print("Type de type records_select : ", type(records_select), "Tous les résultats ", records_select,
              "Type des résultats ")

        for row in records_select:
            print(row['id_genre'], row['intitule_genre'])

        for row in records_select:
            output = "id: {id_genre}  genre: {intitule_genre}"
            print(output.format(**row))

        # Le meilleur pour la fin : le module pymysql intègre la conversion en JSON  avec "cursorclass=pymysql.cursors.DictCursor"
        # Pour vous prouver ceci, il faut importer le module JSON et vous comparer le résultat des print ci-dessous
        # Il faut absolument approcher le format JSON
        # https://developer.mozilla.org/fr/docs/Learn/JavaScript/Objects/JSON
        print("Tous les résultats déjà en JSON ", records_select)
        print(json.dumps(records_select))
        print(json.dumps(records_select, sort_keys=True, indent=4, separators=(',', ': '), default=str))

    except Exception as erreur:
        # OM 2020.03.01 Message en cas d'échec du bon déroulement des commandes ci-dessus.
        print("error message: {0}".format(erreur))
        #render_template('erreur.html', val_erreur_fichier_html=erreur)
        #redirect(url_for('page_not_found'), val_erreur_fichier_html=erreur)
        return render_template('index_1.html')
    return render_template('genres/genres.html', genres=records_select)


#
# Une route est définie, une page HTML s'ouvre, on entre deux 2 paramètres dans un formulaire HTML
# Méthode POST (lecture
# http://127.0.0.1:5002/input_2_champs
#
@obj_mon_application.route("/input_2_champs", methods=["POST"])
def input_post_fields():
    # Récupère les deux "contenus" dans le formulaire du fichier "form_input_2_fields.html"
    val_ici_nom_utilisateur = request.form.get('nom_utilisateur_html')
    val_ici_prenom_utilisateur = request.form.get('prenom_utilisateur_html')
    # Affiche les 2 variables récupérées dans la page HTML
    print(val_ici_nom_utilisateur, "   ", val_ici_prenom_utilisateur)
    # On fait référence au fichier html avec un formulaire ou on entre deux valeurs
    # "nom_utilisateur_html" et "prenom_utilisateur_html"
    return render_template("form_input_2_fields.html")


#
# Une route est définie, une page HTML s'ouvre, on entre deux 2 paramètres dans un formulaire HTML
# on clique sur SUBMIT et les 2 paramètres s'affichent en couleur sur la même page HTML
# http://127.0.0.1:5002/input_2_champs_retour_colore
#
@obj_mon_application.route("/input_2_champs_retour_colore", methods=["POST", "GET"])
def traitement_input_post_get_fields():
    # Récupère les deux "contenus" dans le formulaire du fichier "form_input_2_fields.html"
    val_ici_nom_utilisateur = request.form.get('nom_utilisateur_html')
    val_ici_prenom_utilisateur = request.form.get('prenom_utilisateur_html')
    # Affiche les 2 variables récupérées dans la page HTML
    print(val_ici_nom_utilisateur, "   ", val_ici_prenom_utilisateur)
    # On fait référence au fichier html avec un formulaire ou on entre deux valeurs
    # "nom_utilisateur_html" et "prenom_utilisateur_html"
    return render_template("form_input_2_fields_post_get.html",
                           nom_utilisateur_fichier_html=val_ici_nom_utilisateur,
                           prenom_utilisateur_fichier_html=val_ici_prenom_utilisateur)


if __name__ == "__main__":
    # C'est bien le script principal "__main__" donc on l'interprète (démarre la démo d'utilisation de Flask).
    # Pour montrer qu'on peut paramétrer Flask :
    # On active le mode DEBUG
    # L'adresse IP du serveur mis en place par Flask pourrait être changée.
    # Pour ce fichier "2_debut_flask_4_routes.py" on change le numéro du port par défaut.
    obj_mon_application.run(debug=True,
                            host="127.0.0.1",
                            port="5002")
