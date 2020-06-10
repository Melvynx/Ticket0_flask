from flask import request, jsonify, make_response, flash, url_for, redirect

from app import app
from app.db.query import query
from app.utils import sql_requests


# @app.route("/labels", methods=["POST"])
# def new_label():
#     name = request.form.get("label-name")
#     description = request.form.get("label-description")
#     color = request.form.get("label-color")

#     values = {"name": name, "description": description}
#     #  todo : catch error on front
#     result = query(sql_requests.create_label, values)
#     if result:
#         flash("Item create successful !", "success")
#     else:
#         flash("Can't create item with empty value.", "danger")
#     return redirect(url_for("category"))


@app.route("/labels/<id_label>", methods=["PATCH"])
def edit_label(id_label):
    print("JS SUIS LA PUTE")
    data = request.get_json()

    if not "label" in data:
        status = jsonify(status="need label object", state="danger",)
        return make_response(status, 400)

    label = data["label"]

    if not "name" in label and not "color" in label and not "description" in label:
        status = jsonify(
            status="need name, level and description string", state="danger",
        )
        return make_response(status, 400)

    if not id_label.isdigit():
        status = jsonify(status="url value error", state="danger",)
        return make_response(status, 400)

    values = {
        "name": label["name"],
        "description": label["description"],
        "color": label["color"],
        "id_label": id_label,
    }

    result = query(sql_requests.edit_label, values)

    if result:
        status = jsonify(status="label update successful", state="success")
    else:
        status = jsonify(status="Database has problem.", state="danger")

    return make_response(status, 200)


@app.route("/labels", methods=["POST"])
def create_label_mon():
    data = request.get_json()

    if not "label" in data:
        status = jsonify(status="need label object", state="danger",)
        return make_response(status, 400)

    label = data["label"]

    if not "name" in label and not "color" in label and not "description" in label:
        status = jsonify(
            status="need name, level and description string", state="danger",
        )
        return make_response(status, 400)

    values = {
        "name": "TTTTTT",
        "description": "ok ta mère",
        "color": "101010",
    }

    result = query(sql_requests.create_label, values)

    if result:
        status = jsonify(status="label update successful", state="success")
    else:
        status = jsonify(status="Database has problem.", state="danger")

    return make_response(status, 200)


@app.route("/labels/<id_label>", methods=["DELETE"])
def delete_label(id_label):
    result = query(sql_requests.delete_key_label, {"id_label": id_label})
    result = query(sql_requests.delete_label, {"id_label": id_label})

    if result:
        status = jsonify(status="item deleted successful", state="success")
    else:
        status = jsonify(status="Database has problem.", state="danger")
    return make_response(status, 200)


@app.route("/labels/tiqets/<id_tiqet>", methods=["GET"])
def labels_tiqet(id_tiqet):
    labels = query(
        sql_requests.show_label_by_tiqet, {"id_tiqet": id_tiqet}, fetch="all"
    )

    labelsJson = jsonify(labels)
    return make_response(labelsJson, 200)


@app.route("/labels/<id_label>/tiqets/<id_tiqet>", methods=["POST"])
def create_labels_tiqet(id_label, id_tiqet):
    result = query(
        sql_requests.create_tiqet_label_reation,
        {"id_tiqet": id_tiqet, "id_label": id_label},
    )

    if result:
        status = jsonify(status="label created successful", state="success")
    else:
        status = jsonify(status="Error", state="success")

    return make_response(status, 200)


@app.route("/labels/<id_label>/tiqets/<id_tiqet>", methods=["DELETE"])
def delete_labels_tiqet(id_label, id_tiqet):
    result = query(
        sql_requests.delete_tiqet_label_reation,
        {"id_tiqet": id_tiqet, "id_label": id_label},
    )

    if result:
        status = jsonify(status="label deleted successful", state="success")
    else:
        status = jsonify(status="Error.", state="success")

    return make_response(status, 200)


# @app.route("/items/<id_item>", methods=["PATCH"])
# def item_edit(id_item):
#     data = request.get_json()
#     item_data = data["item"]
#     values = {
#         "name": item_data["name"],
#         "description": item_data["description"],
#         "id": id_item,
#     }
#     response = query(sql_requests.update_item, values)
#     if response:
#         status = jsonify(status="item has been updated", state="success")
#         return make_response(status, 200)
#     status = jsonify(status="sql server has problem", state="danger")
#     return make_response(status, 201)
