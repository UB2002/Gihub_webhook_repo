from flask_cors import CORS
from flask import Flask

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:3000", "https://gihub-webhook-repo.vercel.app"], supports_credentials=True, allow_headers="*")
    from app.app import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app  