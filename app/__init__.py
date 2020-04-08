# Un objet "obj_mon_application" pour utiliser la classe Flask
# Pour les personnes qui veulent savoir ce que signifie __name__ une démonstration se trouve ici :
# https://www.studytonight.com/python/_name_-as-main-method-in-python
# C'est une chaîne de caractère qui permet de savoir si on exécute le code comme script principal
# appelé directement avec Python et pas importé.
from flask import Flask

app = Flask(__name__, template_folder="templates")
# Flask va pouvoir crypter les cookies
app.secret_key = 'LE_VOGON^^^ÂMIRLA'

from app import routes
from app.controller.page import category_page, dashboard_page, item_page, tiqet_page
from app.controller.api import category_api, item_api