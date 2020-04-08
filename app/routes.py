from flask import request, render_template, redirect, url_for, flash, make_response, jsonify

from app.db.SELECT import select_db
from app.db.INSERT import insert

from app import app
from app.utils import sql_requests


@app.errorhandler(404)
def page_not_found(error):
  # Afficher un message dans la console
  app.logger.info(f"L'URL est fausse... {request.url}")
  return render_template("error.html", error=error), 404


# --------------
# | Dashboard |
# --------------

@app.route("/")
@app.route("/dashboard")
@app.route("/home")
def dashboard():
  tiqets = select_db.DBSelect().select(sql_requests.index_tiqet)
  states = select_db.DBSelect().select(sql_requests.index_state)
  return render_template("dashboard.html", title="Dashboard", tiqets=tiqets, states=states)


@app.route("/tiqet/new")
@app.route("/new")
def new():
  categories_db = select_db.DBSelect().select(sql_requests.index_category)
  priorities_db = select_db.DBSelect().select(sql_requests.index_priorities)
  return render_template("new_tiqet.html", title="Create TiQet", categories=categories_db, priorities=priorities_db)


# --------------
# | CATEGORIES |
# --------------

@app.route("/categories")
def categories():
  categories_db = select_db.DBSelect().select(sql_requests.index_category)
  return render_template('categories.html', title="Categories index", title_setting="Categories",
                         categories=categories_db)


@app.route("/category/<id_category>", methods=["GET"])
def category(id_category):
  value = {"id_category": id_category}
  category_db = select_db.DBSelect().select(sql_requests.show_category, value)
  items = select_db.DBSelect().select(sql_requests.show_item_by_category, value)
  return render_template('category.html', title="Category", title_setting="Category", category=category_db, items=items)


@app.route("/category", methods=["POST"])
def category_new():
  name = request.form.get('category_name')
  description = request.form.get('category_description')

  values = {"name": name, "description": description}
  if len(name) > 1 and len(description) > 1:
    insert.DbInsertOneTable().insert(sql_requests.create_category, values)
    flash("Category create successful !", "success")
  else:
    flash("Can't create category with empty value.", "danger")
  return redirect(url_for("categories"))


@app.route("/categories/<id_category>", methods=["PATCH"])
def category_edit(id_category):
  data = request.get_json()
  category_data = data["category"]

  values = {"name": category_data["name"], "description": category_data["description"], "id": id_category}
  response = insert.DbInsertOneTable().insert(sql_requests.update_category, values)
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
  values = {"name": item_data["name"], "description": item_data["description"], "id": id_item}
  response = insert.DbInsertOneTable().insert(sql_requests.update_item, values)
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

  values = {"id_category": category_id, "name": name, "description": description}
  if len(name) > 1 and len(description) > 1:
    insert.DbInsertOneTable().insert(sql_requests.create_item, values)
    flash("Item create successful !", "success")
  else:
    flash("Can't create item with empty value.", "danger")
  return redirect(url_for("category", id_category=category_id))


@app.route("/items/<id_category>", methods=["GET"])
def items_category(id_category):
  items = select_db.DBSelect().select(sql_requests.show_item_by_category, {"id_category": id_category})
  itemsJSON = jsonify(items)
  print(itemsJSON)
  return make_response(itemsJSON, 200)
