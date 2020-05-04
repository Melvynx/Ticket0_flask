from flask import render_template

from app import app
from app.db.query import query
from app.utils import sql_requests


@app.route("/priorities")
def priorities():
    priorities_db = query(sql_requests.index_priorities, fetch="all")
    return render_template(
        "settings/priority/priorities.html",
        title="Priorities",
        priorities=priorities_db,
        title_setting="Priority",
    )
