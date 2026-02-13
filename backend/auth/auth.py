from flask import Blueprint, request, jsonify
import json

auth_bp = Blueprint("auth", __name__)

def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return []

@auth_bp.route("/auth/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    users = load_users()
    user = next((u for u in users if u["username"] == username and u["password"] == password), None)

    if user:
        token = f"{username}-token"
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401
