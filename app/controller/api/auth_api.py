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
    response = make_response(redirect(url_for("dashboard")))
    response.set_cookie(
        "current-user-token", token, samesite=None, max_age=60 * 60 * 24 * 365 * 2
    )
    return response, 200


@app.route("/auth/new", methods=["POST"])
def create_account():
    # nothing to test because all is try in front web
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

    email = query(sql_requests.auth_check_email, {"email": auth["email"]}, fetch="one")
    if email:
        status = jsonify(
            status="Email is alredy take.", username=True, email=False, state="success",
        )
    else:
        status = jsonify(status="All ok", username=True, email=True, state="success",)

    return make_response(status, 200)


@app.route("/auth/<id_user>", methods=["PATCH"])
def edit_user(id_user):
    data = request.get_json()

    if not "auth" in data:
        status = jsonify(status="need auth object", state="danger",)
        return make_response(status, 400)

    auth = data["auth"]

    if not "email" in auth:
        status = jsonify(status="need email object in auth", state="danger",)
        return make_response(status, 400)

    values = {
        "email": auth["email"],
        "firstname": auth["firstname"],
        "lastname": auth["lastname"],
        "id_user": id_user,
    }

    result = query(sql_requests.auth_safe_edit, values)

    if result:
        status = jsonify(status="user edit successful", state="success")
    else:
        status = jsonify(status="Database has problem.", state="danger")

    return make_response(status, 200)


@app.route("/auth/password/<id_user>", methods=["PATCH"])
def edit_user_password(id_user):
    data = request.get_json()

    if not "auth" in data:
        status = jsonify(status="need auth object", state="danger",)
        return make_response(status, 400)

    auth = data["auth"]

    if (
        not "old_password" in auth
        and not "new_password" in auth
        or not "user_cookie" in auth
    ):
        status = jsonify(status="need old_password and new_password", state="danger",)
        return make_response(status, 400)

    if not auth["user_cookie"]:
        status = jsonify(status="invalid user token, are you lost ?", state="danger",)
        return make_response(status, 200)

    user = User()

    if not user.find_by_token(auth["user_cookie"]):
        status = jsonify(status="inccorect user token, are you lost?", state="danger",)
        return make_response(status, 400)
    print("s pa")
    if not user.edit_password(auth["old_password"], auth["new_password"]):
        status = jsonify(status="invalid old password", state="danger",)
        return make_response(status, 200)
    print("e pa")
    status = jsonify(
        status="the password has been changed successfully", state="success",
    )
    return make_response(status, 200)


@app.route("/auth/logout", methods=["GET"])
def logout():
    flash("logout successful", "success")
    response = make_response(redirect(url_for("dashboard")))
    response.set_cookie("current-user-token", "", samesite=None, max_age=1)
    return response, 200
