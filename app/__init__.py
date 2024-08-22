from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os




db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    #app.config.from_object(Config)
    app.config["DATABASE_URL"]="sqlite:///app.db"
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///app.db"
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    """if not os.path.exists(Config.UPLOAD_FOLDER):
        os.makedirs(Config.UPLOAD_FOLDER)"""

    # Register blueprints
    from .routes import register_blue_prints
    register_blue_prints(app)
    
    with app.app_context():
        db.create_all()
        from app.models.model import User
        new_user = User(username="kal",password="9866544",role="Admin")
        db.session.add(new_user)
        db.session.commit()
    
    return app
