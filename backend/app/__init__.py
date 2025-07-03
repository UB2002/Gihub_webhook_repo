from flask_cors import CORS
from flask import Flask

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:4000"])  # Allow CORS from frontend
    from app.app import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app  