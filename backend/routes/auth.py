from flask import Blueprint, request, jsonify
import json
from flask_bcrypt import Bcrypt

auth_bp = Blueprint("auth", __name__)
bcrypt = Bcrypt()

USERS_FILE = "data/users.json"

def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

@auth_bp.route("/auth/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    users = load_users()
    user = next((u for u in users if u["username"] == username), None)

    # ✅ Check password using bcrypt
    if user and bcrypt.check_password_hash(user["password"], password):
        token = f"{username}-token"
        return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"}), 401