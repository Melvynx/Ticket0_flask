from flask import render_template, request, flash, url_for, redirect

from app import app
from app.db.INSERT import insert
from app.db.SELECT import select_db
from app.utils import sql_requests


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