from flask import render_template, request, redirect, url_for, flash, jsonify, make_response

from app import app
from app.db.query import query
from app.utils import sql_requests


@app.route("/tiqet/new")
@app.route("/new")
def new():
  categories_db = query(sql_requests.index_category, fetch="all")
  priorities_db = query(sql_requests.index_priorities, fetch="all")
  users_db = query(sql_requests.index_users_admin, fetch="all")
  return render_template("new_tiqet.html", title="Create TiQet",
                         categories=categories_db, priorities=priorities_db,
                         users=users_db)

