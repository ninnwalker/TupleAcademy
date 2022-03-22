from flask import Blueprint, make_response

from app.models import UserModel

from app.database import session


user_route = Blueprint("user_route", __name__, url_prefix="/user")


@user_route.route("/", methods=["GET"])
def user_index():

    return make_response({"key":"hello"})
