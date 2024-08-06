from flask import Blueprint, render_template, redirect, url_for, session, request, flash
'''from werkzeug.utils import secure_filename
from app import db
import os'''

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')


@main_bp.route('/contact')
def contact():
    return render_template('contact.html')

@main_bp.route('/hero-upload')
def upload_hero(request):
    '''if request.method == 'POST':
        description = request.form['description']
        image_file = request.files.get('image')
        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(os.getenv('UPLOAD_FOLDER'), filename)
            image_file.save(image_path)
            image = filename
        db.session.commit()
        flash('Product Add successfully.', 'success')
        return redirect(url_for('admin.admin'))'''
    return render_template('index.html')

@main_bp.route('/home-about-uplaod')
def home_about():
    '''if request.method == 'POST':
        image_file = request.files.get('image')
        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(os.getenv('UPLOAD_FOLDER'), filename)
            image_file.save(image_path)
            image = filename
        db.session.commit()
        flash('Product Add successfully.', 'success')
        return redirect(url_for('admin.admin'))'''
    return render_template('index.html')