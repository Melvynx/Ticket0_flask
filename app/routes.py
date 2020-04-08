from flask import request, render_template, redirect, url_for, flash, make_response, jsonify

from app.db.SELECT import select_db
from app.db.INSERT import insert

from app import app
from app.utils import sql_requests


@app.errorhandler(404)
def page_not_found(error):
  # Afficher un message dans la console
  app.logger.info(f"L'URL est fausse... {request.url}")
  return render_template("error.html", error=error), 404

