from flask import Blueprint, request, jsonify
from app.controllers.auth_controllers import login, signup

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup_route():
    return signup(request)

@auth_bp.route("/login", methods=["POST"])
def login_route():
    return login(request)
