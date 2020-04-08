# 0_mon_premier_hello_avec_flask.py
# OM 2020.03.29 Démonstration de l'utilisation du microframework Flask
# Sans le traitement des erreurs.

# Importation de la Class Flask
from flask import Flask

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
    return "<h1>Le bonheur en 2020</h1><h3>Rester chez soi !<h3><h6>Hello world!</h6>"


if __name__ == "__main__":
    # C'est bien le script principal "__main__" donc on l'interprète (démarre la démo d'utilisation de Flask).
    obj_mon_application.run()