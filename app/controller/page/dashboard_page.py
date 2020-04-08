from flask import render_template

from app import app
from app.db.SELECT import select_db
from app.utils import sql_requests


@app.route("/")
@app.route("/dashboard")
@app.route("/home")
def dashboard():
  tiqets = select_db.DBSelect().select(sql_requests.index_tiqet)
  states = select_db.DBSelect().select(sql_requests.index_state)
  return render_template("dashboard.html", title="Dashboard", tiqets=tiqets, states=states)
