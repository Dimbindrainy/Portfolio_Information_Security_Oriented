import json
from flask import Blueprint, jsonify
import os

skills_bp = Blueprint("skills_bp", __name__)

DATA_PATH = os.path.join("data", "skills.json")

@skills_bp.route("/skills", methods=["GET"])
def get_skills():
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return jsonify(data)