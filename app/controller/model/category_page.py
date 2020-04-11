from flask import render_template, request, flash, url_for, redirect

from app import app
from app.db.query import query
from app.utils import sql_requests


@app.route("/categories")
def categories():
    categories_db = query(sql_requests.index_category, fetch="all")
    return render_template(
        "categories.html",
        title="Categories index",
        title_setting="Categories",
        categories=categories_db,
    )


@app.route("/category/<id_category>", methods=["GET"])
def category(id_category):
    value = {"id_category": id_category}
    category_db = query(sql_requests.show_category, value, fetch="one")
    items = query(sql_requests.show_item_by_category, value, fetch="all")
    return render_template(
        "category.html",
        title="Category",
        title_setting="Category",
        category=category_db,
        items=items,
    )


@app.route("/category", methods=["POST"])
def category_new():
    name = request.form.get("category_name")
    description = request.form.get("category_description")
    # todo -> meilleur verification
    values = {"name": name, "description": description}

    result = query(sql_requests.create_category, values)
    if result:
        flash("Category create successful !", "success")
    else:
        flash("Can't create category with empty value.", "danger")

    return redirect(url_for("categories"))
