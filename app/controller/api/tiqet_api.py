from flask import request, jsonify, make_response, flash, redirect, url_for

from app import app
from app.db.query import query
from app.utils import sql_requests


# edit how many values we want with this function
@app.route("/tiqet/<id_tiqet>", methods=["PATCH"])
def edit_tiqet(id_tiqet):
    data = request.get_json()
    tiqet = data["tiqet"]
    request_edit_tiqet = sql_requests.tiqet_edit_request(tiqet, id_tiqet)
    response = query(request_edit_tiqet, tiqet)
    if response:
        status = jsonify(status="tiqet's update successful", state="success")
        return make_response(status, 200)
    status = jsonify(status="Database server has problem !", state="danger")
    return make_response(status, 201)


@app.route("/tiqet", methods=["POST"])
def create_tiqet():
    title = request.form.get("tiqet-title")
    content = request.form.get("tiqet-description")
    id_item = request.form.get("tiqet-item")
    id_priority = request.form.get("tiqet-priority")
    id_user = request.form.get("tiqet-user")
    if id_user == "null":
        id_user = None

    values = {
        "title": title,
        "content": content,
        "id_item": id_item,
        "id_priority": id_priority,
        "id_assigned": id_user,
        "id_reporter": None,
        "id_state": 1,
    }
    result = query(sql_requests.create_tiqet, values)

    if result:
        flash("Tiqet create successful !", "success")
        return redirect(url_for("dashboard"))

    flash("Database server has problem.", "danger")
    return redirect(url_for("new"))
