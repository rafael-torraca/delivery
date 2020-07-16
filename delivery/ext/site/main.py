from flask import Blueprint
from flask import request, render_template
from flask import current_app

bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    current_app.logger.debug("OI eu sou o erro!")
    return render_template("index.html") #return render_template("index.html", name="Alow") name=request.args['name']


@bp.route("/sobre")
def about():
    return render_template("about.html")


@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")