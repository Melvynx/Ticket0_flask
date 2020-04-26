from flask import request, url_for, jsonify, make_response

from app import app
from app.db.query import query
from app.utils import sql_requests


@app.route("/login", methods=["POST"])
def login_account():
    data = request.get_json()

    if not "auth" in data:
        status = jsonify(status="error syntaxe json. Need 'auth'", state="danger")
        return make_response(status, 400)

    auth = data["auth"]

    if not "username" in auth or not "password" in auth:
        status = jsonify(
            status="error syntaxe json. Auth need 'username' and 'password'",
            state="danger",
        )
        return make_response(status, 400)

    username = auth["username"]
    password = auth["password"]
