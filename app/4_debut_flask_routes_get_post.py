# 4_debut_flask_routes_get_post.py
# OM 2020.03.29 Démonstration de l'utilisation du microframework Flask
# Méthode POST et GET (plus de renseignements ci-dessous)
# https://www.w3schools.com/tags/ref_httpmethods.asp
# Le retour des données se fait grâce à une page en HTML et le langage JINJA
# Avec le traitement de l'erreur 404.

# Importation de la Class Flask
from flask import Flask, render_template, request

# Un objet "obj_mon_application" pour utiliser la classe Flask
# Pour les personnes qui veulent savoir ce que signifie __name__ une démonstration se trouve ici :
# https://www.studytonight.com/python/_name_-as-main-method-in-python
# C'est une chaîne de caractère qui permet de savoir si on exécute le code comme script principal
# appelé directement avec Python et pas importé.
obj_mon_application = Flask(__name__, template_folder='../templates')

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


#
# Une route est définie, une page HTML s'ouvre, on entre deux 2 paramètres dans un formulaire HTML
# La méthode "GET" est indispensable car on envoie au navigateur le code HTML pour afficher la page
# Méthode POST va permettre de récupérer les valeurs des deux champs INPUT définis dans le fichier
# "form_input_2_fields.html"
# http://127.0.0.1:5002/input_2_champs
#
@obj_mon_application.route("/input_2_champs", methods=["POST", "GET"])
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
    # Pour ce fichier on change le numéro du port par défaut.
    obj_mon_application.run(debug=True,
                            host="127.0.0.1",
                            port="5002")
