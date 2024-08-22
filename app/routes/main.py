from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from werkzeug.utils import secure_filename
import os
from app.__init__ import db

from app.models.model import User

# Create a blueprint for the main application
main_bp = Blueprint('main', __name__)

# Define the upload folder (make sure this directory exists)
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')  # Default to 'uploads' folder

# Function to check allowed file extensions
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main_bp.route('/')
def home():
    new_user = User(username="kal",password="9866544",role="Admin")
    db.session.add(new_user)
    db.session.commit()
    return render_template('index.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')

@main_bp.route('/hero-upload', methods=['GET', 'POST'])
def upload_hero():
    if request.method == 'POST':
        description = request.form.get('description')
        image_file = request.files.get('image')
        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            image_file.save(image_path)
            # Save the image path to the database or perform other actions here
            flash('Hero image uploaded successfully.', 'success')
            return redirect(url_for('main.home'))  # Change redirect to a suitable route
        else:
            flash('Invalid file type. Please upload an image.', 'danger')
    return render_template('upload_hero.html')  # Create this template

@main_bp.route('/home-about-upload', methods=['GET', 'POST'])
def home_about_upload():
    if request.method == 'POST':
        image_file = request.files.get('image')
        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            image_file.save(image_path)
            # Save the image path to the database or perform other actions here
            flash('About image uploaded successfully.', 'success')
            return redirect(url_for('main.home'))  # Change redirect to a suitable route
        else:
            flash('Invalid file type. Please upload an image.', 'danger')
    return render_template('upload_home_about.html')  # Create this template

@main_bp.route('/shopdetails')
def shopdetails():
    return render_template('shopdetails.html')

