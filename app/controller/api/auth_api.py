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


@app.route("/login", methods=["POST"])
def login_account():
    # data = request.get_json()

    # if not "auth" in data:
    #     status = jsonify(status="error syntaxe json. Need 'auth'", state="danger")
    #     return make_response(status, 400)

    # auth = data["auth"]

    # if not "username" in auth or not "password" in auth:
    #     status = jsonify(
    #         status="error syntaxe json. Auth need 'username' and 'password'",
    #         state="danger",
    #     )
    #     return make_response(status, 400)

    username = request.form.get("auth-username")
    password = request.form.get("auth-password")

    user = User(username)

    if not user.find_by_username():
        flash("username doesn't match", "danger")
        return redirect(url_for("login"))

    if not user.check_password(password):
        flash("wrong password", "danger")
        return redirect(url_for("login"))

    token = user.generate_cookie_id()

    if not token:
        flash("error", "danger")
        return redirect(url_for("login"))

    flash("login successful", "success")
    response = make_response(redirect("dashboard"))
    response.set_cookie(
        "current-user-token", token, samesite=None, max_age=60 * 60 * 24 * 365 * 2
    )
    return response, 200
