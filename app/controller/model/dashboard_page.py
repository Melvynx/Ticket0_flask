from flask import render_template

from app import app
from app.db.query import query
from app.utils import sql_requests


@app.route("/")
@app.route("/dashboard")
@app.route("/home")
def dashboard():
    tiqets = query(sql_requests.index_tiqet, fetch="all")
    states = query(sql_requests.index_state, fetch="all")
    return render_template(
        "dashboard.html", title="Dashboard", tiqets=tiqets, states=states
    )
