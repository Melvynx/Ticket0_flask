from flask import request, jsonify, make_response, flash, url_for, redirect

from app import app
from app.db.query import query
from app.utils import sql_requests


@app.route("/items", methods=["POST"])
def item_new():
    name = request.form.get("item-name")
    description = request.form.get("item-description")
    category_id = request.form.get("category-id")

    values = {"id_category": category_id, "name": name, "description": description}
    #  todo : catch error on front
    result = query(sql_requests.create_item, values)
    if result:
        flash("Item create successful !", "success")
    else:
        flash("Can't create item with empty value.", "danger")
    return redirect(url_for("category", id_category=category_id))


@app.route("/items/<id_item>", methods=["DELETE"])
def delete_item(id_item):
    result = query(sql_requests.delete_item, {"id_item": id_item})
    result = query(sql_requests.delete_item_2, {"id_item": id_item})

    if result:
        status = jsonify(status="item deleted successful", state="success")
    else:
        status = jsonify(status="Database has problem.", state="danger")
    return make_response(status, 200)


@app.route("/items/<id_category>", methods=["GET"])
def items_category(id_category):
    items = query(
        sql_requests.show_item_by_category, {"id_category": id_category}, fetch="all"
    )
    itemsJSON = jsonify(items)
    return make_response(itemsJSON, 200)


@app.route("/items/<id_item>", methods=["PATCH"])
def item_edit(id_item):
    data = request.get_json()
    item_data = data["item"]
    values = {
        "name": item_data["name"],
        "description": item_data["description"],
        "id": id_item,
    }
    response = query(sql_requests.update_item, values)
    if response:
        status = jsonify(status="item has been updated", state="success")
        return make_response(status, 200)
    status = jsonify(status="sql server has problem", state="danger")
    return make_response(status, 201)
