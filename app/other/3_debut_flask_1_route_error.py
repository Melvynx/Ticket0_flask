# 3_debut_flask_1_route_error.py
# OM 2020.03.29 Démonstration de l'utilisation du microframework Flask
# Des routes différentes sont définies
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
    return render_template("erreur.html",val_erreur_fichier_html=error), 404


#
#
# Une route est définie avec des paramètres à entrer dans l'URL du navigateur
# http://127.0.0.1:5002/une_cinquieme_route_avec_args/?argument1=valeur1&argument2=valeur2
#
# Pour des détails techniques voir votre module 100 ou ici :
# https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL
# Pour des infos techniques vraies, rendez-vous directement à la source de la connaissance (proche de 8201 [m])
# https://tools.ietf.org/html/rfc3986#section-6.2.3
#
# Après avoir cliqué sur l'url ci-dessous changer les valeurs "Damon" et "Matt"
# Pour la tester http://127.0.0.1:5002/une_cinquieme_route_avec_args/?nom_utilisateur=Damon&prenom_utilisateur=Matt
#
# Pour la tester http://127.0.0.1:5002/une_cinquieme_route_avec_args/?nom_utilisateur=&prenom_utilisateur=Matt
#
@obj_mon_application.route("/une_cinquieme_route_avec_args/")
def traitement_input_url_args():
    # Récupère la valeur de l'url dans le navigateur.
    nom_url_total_route = request.base_url

    # Récupère les deux arguments dans la barre d'URL
    val_ici_nom_utilisateur = request.args.get('nom_utilisateur')
    val_ici_prenom_utilisateur = request.args.get('prenom_utilisateur')

    # Une autre façon de récupérer les 2 arguments de l'URL, cela peut donner des idées à des personnes.
    dict_args_url = request.args
    print(dict_args_url, type(dict_args_url))

    # Pour montrer à l'utilisateur que c'est la méthode GET qui est utilisée pour envoyer les paramètres
    # La méthode GET est la valeur de méthode par défaut.
    # Avec cette méthode, les données du formulaire sont encodées dans une URL.
    # On l'utilise souvent sauf si on ne veut pas que les paramètres soient ajoutés à l'URL.
    methode_utilisee_param = request.method

    # Dans le fichier "templates/about_avec_args.html" on récupère les 3 variables
    # "nom_utilisateur_fichier_html", "prenom_utilisateur_fichier_html" et "nom_complet_url_fichier_html"
    return render_template("about_avec_args.html",
                           nom_utilisateur_fichier_html=val_ici_nom_utilisateur,
                           prenom_utilisateur_fichier_html=val_ici_prenom_utilisateur,
                           nom_complet_url_route_fichier_html=nom_url_total_route,
                           methode_utilisee_param_fichier_html=methode_utilisee_param)


if __name__ == "__main__":
    # C'est bien le script principal "__main__" donc on l'interprète (démarre la démo d'utilisation de Flask).
    # Pour montrer qu'on peut paramétrer Flask :
    # On active le mode DEBUG
    # L'adresse IP du serveur mis en place par Flask pourrait être changée.
    # Pour ce fichier on change le numéro du port par défaut.
    obj_mon_application.run(debug=True,
                            host="127.0.0.1",
                            port="5003")
