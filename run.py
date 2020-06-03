# run.py
#
# MM 8 avril 2020
# file for run flask app
from flask import flash, render_template
from app import app


#  source /Users/melvynmalherbe/Dev/Python/Tiqeto_Epsic.OM/venv/bin/activate
#  to go in venv


@app.errorhandler(Exception)
def exception(error):
    flash(error, "Danger")
    return render_template("error.html")


if __name__ == "__main__":
    # C'est bien le script principal "__main__" donc on l'interprète (démarre la démo d'utilisation de Flask).
    # Pour montrer qu'on peut paramétrer Flask :
    # On active le mode DEBUG
    app.run(debug=True)
