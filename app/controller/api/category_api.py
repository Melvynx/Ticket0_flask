from flask import request, jsonify, make_response

from app import app
from app.db.query import query
from app.utils import sql_requests


@app.route("/categories/<id_category>", methods=["PATCH"])
def category_edit(id_category):
    data = request.get_json()
    category_data = data["category"]

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
