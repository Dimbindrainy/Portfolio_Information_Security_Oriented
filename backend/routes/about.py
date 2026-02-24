import json
import os
from flask import Blueprint, jsonify, request

about_bp = Blueprint("about_bp", __name__)

DATA_PATH = os.path.join("data", "about.json")


@about_bp.route("/about/", methods=["GET"])
def get_about():
    """Return the About JSON data"""
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return jsonify(data)


@about_bp.route("/about/", methods=["PUT"])
def update_about():
    """Update the About JSON file with new data"""
    data = request.json

    # Simple validation: check that required keys exist
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid data"}), 400

    expected_keys = {"headline", "paragraphs", "roles"}
    for key in expected_keys:
        if key not in data:
            # Provide default values if missing
            if key == "headline":
                data[key] = ""
            else:
                data[key] = []

    # Save the updated data
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)

    # Return the updated JSON so frontend can sync
    return jsonify(data)