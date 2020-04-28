from flask import render_template, request, flash, url_for, redirect

from app import app
from app.db.query import query
from app.utils import sql_requests


@app.route("/login", methods=["GET"])
def login():
    return render_template("auth/login.html", title="login")


@app.route("/auth/new", methods=["GET"])
def new_auth():
    return render_template("auth/new.html", title="Make account")


@app.route("/auth/profile", methods=["GET"])
def auth_profile():
    return render_template(
        "settings/auth/auth_profile.html", title_setting="Profile", title="Profile"
    )


@app.route("/auth/security", methods=["GET"])
def auth_security():
    return render_template(
        "settings/auth/auth_security.html", title_setting="Security", title="Profile"
    )
