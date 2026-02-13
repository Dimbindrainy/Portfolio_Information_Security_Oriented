from flask import Flask
from flask_cors import CORS
from routes.projects import projects_bp
from routes.auth import auth_bp

app = Flask(__name__)
CORS(app)  # Allow frontend to fetch data

# Register Blueprints
app.register_blueprint(projects_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)
