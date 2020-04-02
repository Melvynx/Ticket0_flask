# app.py
# MM 2020.04.02
# root file for Flask application

from flask import Flask, request, render_template, redirect, url_for, flash

from db.SELECT import select_db
from db.INSERT import insert

# create object App's Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'DJDDJEOE102939141KXnn'


@app.route("/")
@app.route("/home")
def home():
  route_name = request.base_url
  return f"<h1>First Page</h1><p>you're on {route_name}"


@app.route("/category")
def category():
  categories = select_db.DBSelect().select("SELECT * FROM T_Category")
  return render_template('category_list.html', title="Test", categories=categories)


@app.route("/category/new", methods=["POST"])
def category_new():
  name = request.form.get('category_name')
  description = request.form.get('category_description')

  sql_request = "INSERT INTO `T_Category` (`id_category`, `name`, `description`, `created_at`) VALUES (NULL, %(name)s, %(description)s, CURRENT_TIMESTAMP);"
  values = {"name": name, "description": description}
  if len(name) > 1 and len(description) > 1:
    insert.DbInsertOneTable().insert(sql_request, values)
    flash("Category create successful !", "success")
  else:
    flash("Category don't create.", "danger")
  return redirect(url_for("category"))


@app.errorhandler(404)
def page_not_found(error):
  # Afficher un message dans la console
  app.logger.info(f"L'URL est fausse... {request.url}")
  return render_template("error.html", error=error), 404


@app.route("/form", methods=["POST", "GET"])
def input_post_fields():
  # Récupère les deux "contenus" dans le formulaire du fichier "form_input_2_fields.html"
  name = request.form.get('username')
  message = request.form.get('message')
  # Affiche les 2 variables récupérées dans la page HTML
  print(name, "   ", message)
  # On fait référence au fichier html avec un formulaire ou on entre deux valeurs
  # "nom_utilisateur_html" et "prenom_utilisateur_html"
  return render_template("form.html", name=name, message=message)


if __name__ == "__main__":
  # basic script "__main__"
  app.run(debug=True)
