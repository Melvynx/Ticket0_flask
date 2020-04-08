from flask import render_template

from app import app
from app.db.SELECT import select_db
from app.utils import sql_requests


@app.route("/tiqet/new")
@app.route("/new")
def new():
  categories_db = select_db.DBSelect().select(sql_requests.index_category)
  priorities_db = select_db.DBSelect().select(sql_requests.index_priorities)
  return render_template("new_tiqet.html", title="Create TiQet", categories=categories_db, priorities=priorities_db)


