from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import cloudinary



db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Set up Cloudinary using the config values
    cloudinary.config(
        cloud_name=app.config.get('  '),
        api_key=app.config.get('CLOUDINARY_API_KEY'),
        api_secret=app.config.get('CLOUDINARY_API_SECRET')
    )
    
    """if not os.path.exists(Config.UPLOAD_FOLDER):
        os.makedirs(Config.UPLOAD_FOLDER)"""

    # Register blueprints
    from .routes import register_blue_prints
    register_blue_prints(app)
    
    with app.app_context():
        db.create_all()
        from app.models.model import User
        
        if User.query.filter_by(username="admin").first() not in User.query.all():
            new_user = User(username="admin",password="adim",role="Admin")
            db.session.add(new_user)
            db.session.commit()
            
        
    return app
