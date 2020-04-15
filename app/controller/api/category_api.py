from flask import request, jsonify, make_response

from app import app
from app.db.query import query
from app.utils import sql_requests


@app.route("/categories/<id_category>", methods=["PATCH"])
def category_edit(id_category):
    data = request.get_json()
    # try of object category is on data
    if not "category" in data:
        status = jsonify(status="error syntaxe json. Need 'category'", state="danger")
        return make_response(status, 400)
    category_data = data["category"]
    # try if category have name and description
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
    if True:
        status = jsonify(status="item deleted successful", state="success")
    else:
        status = jsonify(status="Database has problem.", state="danger")

    return make_response(status, 200)
