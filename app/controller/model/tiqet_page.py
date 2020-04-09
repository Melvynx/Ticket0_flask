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


@app.route("/tiqet", methods=["POST"])
def create_tiqet():
  title = request.form.get("tiqet-title")
  content = request.form.get("tiqet-description")
  id_item = request.form.get("tiqet-item")
  id_priority = request.form.get("tiqet-priority")
  id_user = request.form.get("tiqet-user")
  if id_user == "null":
    id_user = None

  values = {"title": title,
            "content": content,
            "id_item": id_item,
            "id_priority": id_priority,
            "id_assigned": id_user,
            "id_reporter": None,
            "id_state": 1}
  result = query(sql_requests.create_tiqet, values)

  if result:
    flash("Tiqet create successful !", "success")
    return redirect(url_for("dashboard"))

  flash("Database server has problem.", "danger")
  return redirect(url_for("new"))
