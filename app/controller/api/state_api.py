from flask import (
    request,
    jsonify,
    make_response,
    url_for,
    flash,
    redirect,
    render_template,
)

from app import app
from app.auth.user import User
from app.db.query import query
from app.utils import sql_requests
from werkzeug.security import generate_password_hash


@app.route("/states/<id_state>", methods=["PATCH"])
def edit_state(id_state):
    data = request.get_json()

    if not "state" in data:
        status = jsonify(status="need state object", state="danger",)
        return make_response(status, 400)

    state = data["state"]

    if not "name" in state and not "display" in state:
        status = jsonify(status="need name and display value", state="danger",)
        return make_response(status, 400)

    if not id_state.isdigit():
        status = jsonify(status="url value error", state="danger",)
        return make_response(status, 400)

    values = {
        "name": state["name"],
        "display": state["display"],
        "id_priority": id_state,
    }

    result = query(sql_requests.edit_state, values)

    if result:
        status = jsonify(status="state update successful", state="success")
    else:
        status = jsonify(status="Database has problem.", state="danger")

    return make_response(status, 200)


@app.route("/states", methods=["POST"])
def create_priority():
    data = request.get_json()

    if not "state" in data:
        status = jsonify(status="need state object", state="danger",)
        return make_response(status, 400)

    state = data["state"]

    if not "name" in state:
        status = jsonify(status="need name and display value", state="danger",)
        return make_response(status, 400)

    values = {
        "name": state["name"],
        "display": True,
    }

    result = query(sql_requests.create_state, values)

    if result:
        status = jsonify(status="state create successful", state="success")
    else:
        status = jsonify(status="Database has problem.", state="danger")

    return make_response(status, 200)


@app.route("/states/<id_state>", methods=["DELETE"])
def delete_priority(id_state):
    result = query(sql_requests.delete_key_state, {"id_state": id_state})
    result = query(sql_requests.delete_state, {"id_state": id_state})

    if result:
        status = jsonify(status="state deleted successful", state="success")
    else:
        status = jsonify(status="Database has problem.", state="danger")
    return make_response(status, 200)
