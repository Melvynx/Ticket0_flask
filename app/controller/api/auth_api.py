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


@app.route("/auth/new", methods=["POST"])
def create_account():
    username = request.form.get("auth-username")
    email = request.form.get("auth-email")
    firstname = request.form.get("auth-firstname")
    lastname = request.form.get("auth-lastname")
    password = request.form.get("auth-password")
    values = {
        "username": username,
        "email": email,
        "firstname": firstname,
        "lastname": lastname,
        "password": generate_password_hash(password),
    }
    query(sql_requests.auth_create, values)
    flash("Account create successful! Login.", "success")
    return redirect(url_for("login"))


@app.route("/auth/check_credential", methods=["POST"])
def check_credential():
    data = request.get_json()

    if not "auth" in data:
        status = jsonify(status="need auth", state="danger",)
        return make_response(status, 400)

    auth = data["auth"]

    if not "username" in auth or not "email" in auth:
        status = jsonify(status="need email and username object", state="danger",)
        return make_response(status, 400)

    username = query(
        sql_requests.auth_check_username, {"username": auth["username"]}, fetch="one"
    )

    if username:
        status = jsonify(
            status="Username is alredy take.",
            username=False,
            email=False,
            state="success",
        )
        return make_response(status, 200)
    print(auth["email"])
    email = query(sql_requests.auth_check_email, {"email": auth["email"]}, fetch="one")
    print(email)
    if email:
        status = jsonify(
            status="Email is alredy take.", username=True, email=False, state="success",
        )
    else:
        status = jsonify(status="All ok", username=True, email=True, state="success",)

    return make_response(status, 200)
