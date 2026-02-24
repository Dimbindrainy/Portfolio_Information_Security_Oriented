from flask import Flask
from flask_cors import CORS
from routes.projects import projects_bp
from routes.auth import auth_bp
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from routes.skills import skills_bp
from routes.about import about_bp


app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret-key-change-this"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600

CORS(app)  # Allow frontend to fetch data

# Register Blueprints
app.register_blueprint(projects_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(skills_bp)
app.register_blueprint(about_bp)


if __name__ == "__main__":
    app.run(debug=True)
