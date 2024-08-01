from flask import Flask
from .config import Config
from .routes import main_bp  # Example of blueprint import

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints
    app.register_blueprint(main_bp)
    
    return app
