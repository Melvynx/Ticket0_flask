from flask import request, jsonify, make_response

from app import app
from app.db.query import query
from app.utils import sql_requests
from app.utils.key import crypt_cookie_key, password_security_key


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

    user = query(
        sql_requests.auth_login,
        {"username": username, "password": password},
        fetch="one",
    )

    if not user:
        status = jsonify(status="wrong user credential", state="danger",)
        return make_response(status, 400)

    # print(encrypt(user["id"], crypt_cookie_key))

    status = jsonify(status="login successful", state="success",)
    return make_response(status, 400)
