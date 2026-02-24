import json
from flask import Blueprint, request, jsonify
import os

skills_bp = Blueprint("skills_bp", __name__)

DATA_PATH = os.path.join("data", "skills.json")

def load_skills():
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_skills(data):
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)

# GET all skills
@skills_bp.route("/skills", methods=["GET"])
def get_skills():
    data = load_skills()
    return jsonify(data)

# ADD new skill/tech/tool
@skills_bp.route("/skills", methods=["POST"])
def add_item():
    data = load_skills()
    body = request.json
    category = body.get("category")  # "skills", "tech_stack", "tools"
    value = body.get("value")        # new item
    if category and value is not None:
        if category == "skills":
            data["skills"].append(value)  # value is dict {category,name}
        elif category == "tech_stack":
            data["tech_stack"].append(value)
        elif category == "tools":
            data["tools"].append(value)
        save_skills(data)
        return jsonify(data)
    return jsonify({"error": "Invalid data"}), 400

# DELETE skill/tech/tool by index
@skills_bp.route("/skills", methods=["DELETE"])
def delete_item():
    data = load_skills()
    body = request.json
    category = body.get("category")  # "skills", "tech_stack", "tools"
    index = body.get("index")        # index to remove
    if category is not None and index is not None:
        try:
            if category == "skills":
                data["skills"].pop(index)
            elif category == "tech_stack":
                data["tech_stack"].pop(index)
            elif category == "tools":
                data["tools"].pop(index)
            save_skills(data)
            return jsonify(data)
        except IndexError:
            return jsonify({"error": "Invalid index"}), 400
    return jsonify({"error": "Invalid data"}), 400