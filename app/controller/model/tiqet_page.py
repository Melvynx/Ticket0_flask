from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify,
    make_response,
)

from app import app
from app.db.query import query
from app.utils import sql_requests


@app.route("/tiqet/new")
@app.route("/new")
def new():
    categories_db = query(sql_requests.index_category, fetch="all")
    priorities_db = query(sql_requests.index_priorities, fetch="all")
    users_db = query(sql_requests.index_users, fetch="all")
    return render_template(
        "new_tiqet/new_tiqet.html",
        title="Create TiQet",
        categories=categories_db,
        priorities=priorities_db,
        users=users_db,
    )


@app.route("/tiqet/<id_tiqet>", methods=["GET"])
def tiqet(id_tiqet):
    tiqet_db = query(sql_requests.show_tiqet, {"id_tiqet": id_tiqet}, fetch="one")
    comments_db = query(sql_requests.index_comment, {"id_tiqet": id_tiqet}, fetch="all")
    return render_template("tiqet/tiqet.html", tiqet=tiqet_db, comments=comments_db)
