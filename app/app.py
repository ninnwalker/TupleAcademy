from flask import Flask, Blueprint, render_template

from app.routes import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("home/index.html")

all_routes = [route for name, route in globals().items() if isinstance(route, Blueprint)]

for route in all_routes:
    app.register_blueprint(route)


def app_factory(app, config=None, with_db=False):

    current_app = app.config.from_object(config) if config else app

    # db = SQLAlchemy(app=current_app)

    return app