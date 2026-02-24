import json
from getpass import getpass
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
USERS_FILE = "data/users.json"

# Load existing users
try:
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
except:
    users = []

# Username
username = input("Enter username: ").strip()

# Password
password = getpass("Enter new password: ").strip()
confirm = getpass("Confirm password: ").strip()
if password != confirm:
    print("Passwords do not match!")
    exit(1)

# Hash password
hashed = bcrypt.generate_password_hash(password).decode("utf-8")

# Update existing or add new
found = False
for user in users:
    if user["username"] == username:
        user["password"] = hashed
        found = True
        break

if not found:
    users.append({"username": username, "password": hashed})

# Save
with open(USERS_FILE, "w") as f:
    json.dump(users, f, indent=2)

print(f"Password set for user '{username}'")