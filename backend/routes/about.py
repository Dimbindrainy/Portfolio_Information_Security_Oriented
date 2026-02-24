import json
import os
from flask import Blueprint, jsonify, request

about_bp = Blueprint("about_bp", __name__)

DATA_PATH = os.path.join("data", "about.json")


@about_bp.route("/about/", methods=["GET"])
def get_about():
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return jsonify(data)


@about_bp.route("/about/", methods=["PUT"])
def update_about():
    data = request.json
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)
    return jsonify({"message": "About section updated"})