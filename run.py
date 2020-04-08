# run_mon_app.py
#
# OM 2020.03.29 Démonstration de l'utilisation du microframework Flask
# Des routes différentes sont définies
# Le retour des données se fait grâce à une page en HTML et le langage JINJA
# Avec le traitement de certaines erreurs.

# Importation de la Class Flask
from flask import flash, render_template
from app import app


@app.errorhandler(Exception)
def exception(error):
  flash(error, "Danger")
  return render_template("home.html")


if __name__ == "__main__":
  # C'est bien le script principal "__main__" donc on l'interprète (démarre la démo d'utilisation de Flask).
  # Pour montrer qu'on peut paramétrer Flask :
  # On active le mode DEBUG
  app.run(debug=True)