from flask import Flask
from .config import Config
from app.routes.main import main_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .routes import register_blue_prints
    register_blue_prints(app)


    
    return app
