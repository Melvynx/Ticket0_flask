from flask import render_template

from app import app
from app.db.query import query
from app.utils import sql_requests


@app.route("/states")
def states():
    states_db = query(sql_requests.index_state, fetch="all")
    return render_template(
        "settings/state/states.html",
        title="States",
        states=states_db,
        title_setting="States",
    )
