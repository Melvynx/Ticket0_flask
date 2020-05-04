from flask import request, jsonify, make_response, flash, redirect, url_for

from app import app
from app.db.query import query
from app.utils import sql_requests


@app.route("/categories/<id_category>", methods=["PATCH"])
def category_edit(id_category):
    data = request.get_json()

    if not "category" in data:
        status = jsonify(status="error syntaxe json. Need 'category'", state="danger")
        return make_response(status, 400)
    category_data = data["category"]

    if not "name" in category_data or not "description" in category_data:
        status = jsonify(
            status="error syntaxe json. Category need 'name' and 'description'",
            state="danger",
        )
        return make_response(status, 400)

    values = {
        "name": category_data["name"],
        "description": category_data["description"],
        "id": id_category,
    }
    response = query(sql_requests.update_category, values)

    if response:
        status = jsonify(status="category has been updated", state="success")
        return make_response(status, 200)
    else:
        status = jsonify(status="sql server has problem", state="danger")
        return make_response(status, 201)


@app.route("/categories/<id_category>", methods=["DELETE"])
def delete_category(id_category):
    result = query(sql_requests.delete_category, {"id_category": id_category})

    if result:
        status = jsonify(status="category deleted successful", state="success")
    else:
        status = jsonify(status="Database has problem.", state="danger")
    return make_response(status, 200)


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
        flash("Database server has problem. Try an other time.", "danger")

    return redirect(url_for("categories"))
