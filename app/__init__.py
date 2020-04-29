# Un objet "obj_mon_application" pour utiliser la classe Flask
# Pour les personnes qui veulent savoir ce que signifie __name__ une démonstration se trouve ici :
# https://www.studytonight.com/python/_name_-as-main-method-in-python
# C'est une chaîne de caractère qui permet de savoir si on exécute le code comme script principal
# appelé directement avec Python et pas importé.
from flask import Flask, render_template, request
from flask_cors import CORS
from app.auth.user import User

app = Flask(__name__, template_folder="templates")

# cors permet de généré automatiquement les droits "allow-origin" etc... Qui permette de répondre
# à la méthod OPTION et donc de pouvoir excectuer la tache !
CORS(app)
# Flask va pouvoir crypter les cookies
app.secret_key = "MGC@@VdpdJr@c/Kp7(H#BO"


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("404/404.html"), 404


@app.context_processor
def inject_user():
    if not request.cookies.get("current-user-token"):
        print("no user")
        return dict()

    token = request.cookies.get("current-user-token")
    user = User()

    if not user.find_by_token(token):
        print("no match with user token")
        return dict()

    return dict(user=user.user)


from app.controller.model import (
    category_page,
    dashboard_page,
    tiqet_page,
    auth_page,
)
from app.controller.api import category_api, item_api, tiqet_api, auth_api, comment_api
