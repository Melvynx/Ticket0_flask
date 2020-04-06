# app.py
# MM 2020.04.02
# root file for Flask application

from flask import Flask, request, render_template, redirect, url_for, flash, make_response, jsonify

from db.SELECT import select_db
from db.INSERT import insert

# create object App's Flask
app = Flask(__name__)

# init SECRET_KEY
app.config['SECRET_KEY'] = 'MaccaudNePeutPasTestCetteApplication4004040404040040404'


@app.route("/")
@app.route("/home")
def home():
  route_name = request.base_url
  return f"<h1>First Page</h1><p>you're on {route_name}"


@app.route("/test")
def test():
  return render_template("test.html", title="Cat", title_setting="cati")


@app.errorhandler(404)
def page_not_found(error):
  # Afficher un message dans la console
  app.logger.info(f"L'URL est fausse... {request.url}")
  return render_template("error.html", error=error), 404

# --------------
# | CATEGORIES |
# --------------


@app.route("/categories")
def categories():
  categories_db = select_db.DBSelect().select("SELECT * FROM T_Category")
  return render_template('categories.html', title="Categories index", title_setting="Categories",
                         categories=categories_db)


@app.route("/category/<id_category>", methods=["GET"])
def category(id_category):
  category_db = select_db.DBSelect().select(f"SELECT * FROM `T_Category` WHERE `id_category` = {id_category} ")
  items = select_db.DBSelect().select(f"SELECT * FROM `T_Item` WHERE `fk_category` = {id_category} ")
  return render_template('category.html', title="Category", title_setting="Category", category=category_db, items=items)


@app.route("/category", methods=["POST"])
def category_new():
  name = request.form.get('category_name')
  description = request.form.get('category_description')

  sql_request = "INSERT INTO `T_Category` (`id_category`, `name`, `description`, `created_at`) VALUES (NULL, " \
                "%(name)s, %(description)s, CURRENT_TIMESTAMP); "
  values = {"name": name, "description": description}
  if len(name) > 1 and len(description) > 1:
    insert.DbInsertOneTable().insert(sql_request, values)
    flash("Category create successful !", "success")
  else:
    flash("Can't create category with empty value.", "danger")
  return redirect(url_for("categories"))


@app.route("/categories/<id_category>", methods=["PATCH"])
def category_edit(id_category):
  data = request.get_json()
  category_data = data["category"]
  sql_request = "UPDATE `T_Category` SET `name` = %(name)s, `description` = %(description)s WHERE " \
                "`T_Category`.`id_category` = %(id)s; "
  values = {"name": category_data["name"], "description": category_data["description"], "id": id_category}
  response = insert.DbInsertOneTable().insert(sql_request, values)
  if response:
    status = jsonify(
      status="category has been updated",
      state="success"
    )
    return make_response(status, 200)
  else:
    status = jsonify(
      status="sql server has problem",
      state="danger"
    )
    return make_response(status, 201)


# --------------
# | ITEM |
# --------------

@app.route("/items/<id_item>", methods=["PATCH"])
def item_edit(id_item):
  data = request.get_json()
  item_data = data["item"]
  sql_request = "UPDATE `T_Item` SET `name` = %(name)s, `description` = %(description)s WHERE `T_Item`.`id_item` = %(" \
                "id)s; "
  values = {"name": item_data["name"], "description": item_data["description"], "id": id_item}
  response = insert.DbInsertOneTable().insert(sql_request, values)
  if response:
    status = jsonify(
      status="item has been updated",
      state="success"
    )
    return make_response(status, 200)
  else:
    status = jsonify(
      status="sql server has problem",
      state="danger"
    )
    return make_response(status, 201)


@app.route("/items", methods=["POST"])
def item_new():
  name = request.form.get('item-name')
  description = request.form.get('item-description')
  category_id = request.form.get('category-id')

  sql_request = "INSERT INTO `T_Item` (`id_item`, `fk_category`, `name`, `description`, `created_at`) VALUES (NULL, " \
                "%(id_category)s, %(name)s, %(description)s, CURRENT_TIMESTAMP); "
  values = {"id_category": category_id, "name": name, "description": description}
  if len(name) > 1 and len(description) > 1:
    insert.DbInsertOneTable().insert(sql_request, values)
    flash("Item create successful !", "success")
  else:
    flash("Can't create item with empty value.", "danger")
  return redirect(url_for("category", id_category=category_id))


# flask auto run
if __name__ == "__main__":
  # basic script "__main__"
  app.run(debug=True)
