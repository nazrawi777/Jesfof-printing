from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os




db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app=app)
    migrate.init_app(app, db)
    
    if not os.path.exists(Config.UPLOAD_FOLDER):
        os.makedirs(Config.UPLOAD_FOLDER)

    # Register blueprints
    from .routes import register_blue_prints
    register_blue_prints(app)
    
    with app.app_context():
        from .models.model import User
        db.create_all()
        
    
    return app
