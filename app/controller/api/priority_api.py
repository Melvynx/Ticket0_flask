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


@app.route("/priorities/<id_priority>", methods=["PATCH"])
def edit_priority(id_priority):
    data = request.get_json()

    if not "priority" in data:
        status = jsonify(status="need priority object", state="danger",)
        return make_response(status, 400)

    priority = data["priority"]

    if (
        not "name" in priority
        and not "level" in priority
        and not "description" in priority
    ):
        status = jsonify(
            status="need name, level and description object", state="danger",
        )
        return make_response(status, 400)

    if not id_priority.isdigit():
        status = jsonify(status="url value error", state="danger",)
        return make_response(status, 400)

    values = {
        "name": priority["name"],
        "description": priority["description"],
        "level": priority["level"],
        "id_priority": id_priority,
    }

    result = query(sql_requests.edit_priority, values)

    if result:
        status = jsonify(status="priority update successful", state="success")
    else:
        status = jsonify(status="Database has problem.", state="danger")

    return make_response(status, 200)


@app.route("/priorities", methods=["POST"])
def create_priority():
    data = request.get_json()

    if not "priority" in data:
        status = jsonify(status="need priority object", state="danger",)
        return make_response(status, 400)

    priority = data["priority"]

    if (
        not "name" in priority
        and not "level" in priority
        and not "description" in priority
    ):
        status = jsonify(
            status="need name, level and description object", state="danger",
        )
        return make_response(status, 400)

    values = {
        "name": priority["name"],
        "description": priority["description"],
        "level": priority["level"],
    }

    result = query(sql_requests.create_priority, values)

    if result:
        status = jsonify(status="priority create successful", state="success")
    else:
        status = jsonify(status="Database has problem.", state="danger")

    return make_response(status, 200)


@app.route("/priorities/<id_priority>", methods=["DELETE"])
def delete_priority(id_priority):
    result = query(sql_requests.delete_key_priority, {"id_priority": id_priority})
    result = query(sql_requests.delete_priority, {"id_priority": id_priority})

    if result:
        status = jsonify(status="priority deleted successful", state="success")
    else:
        status = jsonify(status="Database has problem.", state="danger")
    return make_response(status, 200)
