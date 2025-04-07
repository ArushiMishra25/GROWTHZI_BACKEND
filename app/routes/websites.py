from flask import Blueprint, request
from app.controllers.websites_controller import (
    generate_website,
    get_websites,
    update_website,
    delete_website
)

website_bp = Blueprint("websites", __name__)

@website_bp.route("/generate", methods=["POST"])
def generate_website_route():
    return generate_website(request)

@website_bp.route("/", methods=["GET"])
def get_all_websites():
    return get_websites(request)

@website_bp.route("/<website_id>", methods=["PUT"])
def update_website_route(website_id):
    return update_website(request, website_id)

@website_bp.route("/<website_id>", methods=["DELETE"])
def delete_website_route(website_id):
    return delete_website(request, website_id)
