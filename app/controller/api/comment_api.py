from flask import (
    request,
    jsonify,
    make_response,
    url_for,
    flash,
    redirect,
    render_template,
)

from app import app
from app.auth.user import User
from app.db.query import query
from app.utils import sql_requests
from werkzeug.security import generate_password_hash


@app.route("/comments/<id_tiqet>", methods=["GET"])
def index_comments(id_tiqet):
    comments = query(sql_requests.index_comments, {"id_tiqet": id_tiqet}, fetch="all")

    commentsJson = jsonify(comments)
    return make_response(commentsJson, 200)


@app.route("/comments/<id_tiqet>", methods=["POST"])
def create_comment(id_tiqet):
    data = request.get_json()

    if not "comment" in data:
        status = jsonify(status="need comment object", state="danger",)
        return make_response(status, 400)

    comment = data["comment"]
    if not "content" in comment or not "user_hash" in comment:
        status = jsonify(
            status="need comment content and user_hash object", state="danger",
        )
        return make_response(status, 400)

    user = User()
    if not user.find_by_token(comment["user_hash"]):
        status = jsonify(status="invalid user hash", state="danger",)
        return make_response(status, 200)
    values = {
        "id_user": user.user["id_user"],
        "id_tiqet": id_tiqet,
        "content": comment["content"],
    }


    result = query(sql_requests.create_comment, values)

    if result:
        status = jsonify(status="comment create successful", state="success")
    else:
        status = jsonify(status="Database has problem.", state="danger")

    return make_response(status, 200)
