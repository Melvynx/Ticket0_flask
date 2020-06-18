from flask import render_template

from app import app
from app.db.query import query
from app.utils import sql_requests


@app.route("/labels", methods=["GET"])
def labels():
    labels_db = query(sql_requests.index_label, fetch="all")
    return render_template(
        "settings/label/labels.html",
        title="Labels",
        labels=labels_db,
        title_setting="Labels",
    )
