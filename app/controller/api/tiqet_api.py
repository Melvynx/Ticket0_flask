from flask import request, jsonify, make_response

from app import app
from app.db.query import query
from app.utils import sql_requests


# route api for edit tiqet's state
@app.route("/tiqet/<id_tiqet>/state", methods=["PATCH"])
def tiqet_state(id_tiqet):
  data = request.get_json()
  tiqet = data["tiqet"]
  id_state = tiqet["state"]
  response = query(sql_requests.edit_state_tiqet, {"id_state": id_state, "id_tiqet": id_tiqet})

  if response:
    status = jsonify(
      status="tiqet's state update successful",
      state="success"
    )
    return make_response(status, 200)
  status = jsonify(
    status="sql server has problem !",
    state="danger"
  )
  return make_response(status, 201)
