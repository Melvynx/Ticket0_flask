# 1_flask_4_routes_params.py
# OM 2020.03.29 Démonstration de l'utilisation du microframework Flask
# Sans le traitement des erreurs.

# Importation de la Class Flask
from flask import Flask, request

# Un objet "obj_mon_application" pour utiliser la classe Flask
# Pour les personnes qui veulent savoir ce que signifie __name__ une démonstration se trouve ici :
# https://www.studytonight.com/python/_name_-as-main-method-in-python
# C'est une chaîne de caractère qui permet de savoir si on exécute le code comme script principal
# appelé directement avec Python et pas importé.
obj_mon_application = Flask(__name__)

# Fonction dir() extraordinaire pour explorer les attributs, les fonctions.
print(dir(obj_mon_application))


# Une "route" c'est une URL ou des URL(s) qui permet(tent) d'interpréter la fonction au-dessous.
# Dans Flask, les routes sont déclarées via le décorateur @obj_mon_application.route("/")
@obj_mon_application.route("/")
def index():
    # On affiche une chaîne en format HTML, ici des éléments de titre de section de différentes grandeurs
    return "<h1>flask_3_routes_params Le bonheur en 2020</h1><h3>Rester chez soi !<h3><h6>Hello world!</h6>"


# Une seconde route est définie
# Pour la tester http://127.0.0.1:5000/EnPlusElleEstDroleCetteRoute
@obj_mon_application.route("/EnPlusElleEstDroleCetteRoute")
def afficher_un_texte_dans_browser():
    # On affiche une chaîne en format HTML
    return "<h1>Rester sur sa route et la déchirer... c'est le bonheur en 2020.</h1>"


# Des routes sont définies qui vont déclencher la fonction "la_meme_fonction_pour_trois_routes"
# Pour la tester http://127.0.0.1:5000/la_troisieme_route_3
# Pour la tester http://127.0.0.1:5000/une_autre_route_3
# Pour la tester http://127.0.0.1:5000/bon_la_encore_une_autre_route_3_pfff
@obj_mon_application.route("/la_troisieme_route_3")
@obj_mon_application.route("/une_autre_route_3")
@obj_mon_application.route("/bon_la_encore_une_autre_route_3_pfff")
def la_meme_fonction_pour_trois_routes():
    # Récupère la valeur de l'url dans le navigateur.
    nom_route_1 = request.base_url
    texte_pour_dire_aurevoir = " ciao tutti !!!!"

    # On affiche une chaîne en format HTML avec un affichage de la valeur de la variable
    # "nom_route_1" et "texte_pour_dire_aurevoir" On utilise les f-strings, un truc fantastique de Python
    # https://saralgyaan.com/posts/f-string-in-python-usage-guide/
    return f"<h1>Ouais 3 routes avec des noms différents affichent ce texte.</h1><h2>Vous avez demané l'URL ==> {nom_route_1}  et .. {texte_pour_dire_aurevoir}</h2>"


# Une route est définie avec un paramètre à entrer dans l'URL du BROWSER
# Après avoir cliqué sur l'url ci-dessous changer la chaîne de caractères "ChangerCetteValeur"
# Pour la tester http://127.0.0.1:5000/la_quatrieme_route/ChangerCetteValeur
@obj_mon_application.route("/la_quatrieme_route/<nom_input_url>")
def traitement_param_input_url(nom_input_url):
    # Récupère la valeur de l'url dans le navigateur.
    nom_route_1 = request.base_url

    # OM 2020.03.30 Je ne dois pas expliquer la  ligne ci-dessous... mais je vous assure que
    # c'est de la dentelle en programmation tellement c'est fin...
    # Permet de lire de droite à gauche la chaîne de caractères "ChangerCetteValeur" entrée dans l'url
    # https://docs.python.org/3/tutorial/introduction.html
    reverse_nom_input_url = nom_input_url[::-1]

    # On affiche une chaîne en format HTML avec un affichage de la valeur de la variable
    # "nom_input_url" et "reverse_nom_input_url" On utilise les f-strings, un truc fantastique de Python
    # https://saralgyaan.com/posts/f-string-in-python-usage-guide/
    return f"<h1>Votre paramètre d'entrée :  {nom_input_url}  -------- > dans le sens de lecture inverse : {reverse_nom_input_url}</h2><h4>{nom_route_1}</h4>"


if __name__ == "__main__":
    # C'est bien le script principal "__main__" donc on l'interprète (démarre la démo d'utilisation de Flask).
    obj_mon_application.run()
