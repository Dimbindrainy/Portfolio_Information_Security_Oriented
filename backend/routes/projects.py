from flask import Blueprint, jsonify
import json

projects_bp = Blueprint("projects", __name__)

def load_projects():
    try:
        with open("data/projects.json", "r") as f:
            return json.load(f)
    except:
        return []

@projects_bp.route("/projects/", methods=["GET"])
def get_projects():
    return jsonify(load_projects())
