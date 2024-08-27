from flask import Blueprint, jsonify, render_template, redirect, send_from_directory, url_for, session, request, flash
from werkzeug.utils import secure_filename
import os
from app import db
import cloudinary.uploader # type: ignore
from app.models.model import User,HeroSlider,AboutImges,HeroExpandImage,Clients,HeroVideos,YoutubeVideos

# Create a blueprint for the main application
main_bp = Blueprint('main', __name__)

# Define the upload folder (make sure this directory exists)
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')  # Default to 'uploads' folder

# Function to check allowed file extensions
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main_bp.route('/')
def home():
    hero_slides = HeroSlider.query.all()
    about_imgs = AboutImges.query.all()
    client_logos = Clients.query.all()
    gallery_images = HeroExpandImage.query.all()
    videos = HeroVideos.query.all()
    youtube_links = YoutubeVideos.query.all()
  
 
    return render_template('index.html', data={
      "banners":hero_slides,
       "about_imgs":about_imgs,
      "client_logos":client_logos,
      "gallery_images":gallery_images,
      "videos":videos,
      "youtube_videos":youtube_links,
  })

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')

@main_bp.route('/hero-upload', methods=['GET', 'POST'])
def upload_hero():
    if request.method == 'POST':
        description = request.form.get('image_caption')
        sub_title = request.form.get("sub_title")
        title = request.form.get("sub_title")
        btn_text = request.form.get("btn_text")
        image_file = request.files.get('image')
        if image_file and allowed_file(image_file.filename):
            # Upload image to Cloudinary
            upload_result = cloudinary.uploader.upload(
                image_file, resource_type='auto')
            new_slide = HeroSlider(title=title,sub_title=sub_title,body=description,bg_image_url=upload_result["secure_url"],btn_text=btn_text,public_id=upload_result["public_id"])    
            """filename = secure_filename(image_file.filename)
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            image_file.save(image_path)"""
            db.session.add(new_slide)
            db.session.commit()
            flash('Hero image uploaded successfully.', 'success')
        else:
            flash('Invalid file type. Please upload an image.', 'danger')
    return redirect(url_for("admin.admin"))

@main_bp.route('/home-about-upload', methods=['GET', 'POST'])
def home_about_upload():
    if request.method == 'POST':
        image_file = request.files.get('image')
        #about_text = request.files.get('about_text')
        if image_file and allowed_file(image_file.filename):
            print("Upload About")
            # Upload image to Cloudinary
            upload_result = cloudinary.uploader.upload(
                image_file, resource_type='auto')
            new_about_image = AboutImges(public_id=upload_result["public_id"],img_url=upload_result["secure_url"])
            db.session.add(new_about_image)
            db.session.commit()
            flash('About image uploaded successfully.', 'success')
        else:
            flash('Invalid file type. Please upload an image.', 'danger')
    return redirect(url_for("admin.admin"))


@main_bp.route("/upload/home-expand-images", methods=['GET', 'POST'])
def home_expand_images():
    if request.method == 'POST':
        image_file = request.files.get('image')
        if image_file and allowed_file(image_file.filename):
            print("Test Home")
            upload_result = cloudinary.uploader.upload(
                image_file, resource_type='auto')
            new_about = HeroExpandImage(public_id=upload_result["public_id"],img_url=upload_result["secure_url"])
            db.session.add(new_about)
            db.session.commit()
            flash('About image uploaded successfully.', 'success')
            print('About image uploaded successfully.', 'success')
        else:
            flash('Invalid file type. Please upload an image.', 'danger')
    return redirect(url_for("admin.admin"))


@main_bp.route("/upload/client-logos", methods=['GET', 'POST'])
def home_client_log():
    if request.method == 'POST':
        image_file = request.files.get('logo')
        if image_file and allowed_file(image_file.filename):
            upload_result = cloudinary.uploader.upload(
                image_file, resource_type='auto')
            new_about_image = Clients(public_id=upload_result["public_id"],img_url=upload_result["secure_url"])
            db.session.add(new_about_image)
            db.session.commit()
            
            flash('About image uploaded successfully.', 'success')
        else:
            flash('Invalid file type. Please upload an image.', 'danger')
    return redirect(url_for("admin.admin"))

@main_bp.route("/upload/video-slider", methods=['GET', 'POST'])
def home_video_slider():
    if request.method == 'POST':
        video_file = request.files.get('video')
        if video_file:
            # Upload video to Cloudinary
            upload_result = cloudinary.uploader.upload(
                video_file, resource_type='auto')
            home_video = HeroVideos(public_id=upload_result["public_id"],video_url=upload_result["secure_url"])
            db.session.add(home_video)
            db.session.commit()
            flash('home video uploaded successfully.', 'success')
        else:
            flash('Invalid file type. Please upload an image.', 'danger')
    return redirect(url_for("admin.admin"))

@main_bp.route("/upload/youtube-video", methods=['GET', 'POST'])
def home_youtube_video():
    if request.method == 'POST':
        link = request.form.get('link')
        if link:
            new_url = YoutubeVideos(youtube_url=link)
            db.session.add(new_url)
            db.session.commit()
            flash('File successfully uploaded')
        else:
            flash('error Input Required', 'danger')
    return redirect(url_for("admin.admin"))


@main_bp.route('/shopdetails')
def shopdetails():
    return render_template('shopdetails.html')
    
@main_bp.route("/serve/<filename>")
def serve_imgs(filename):
    try:
        return send_from_directory("upload_folder",filename)
    except Exception:
        print("error")
        return "Error"

@main_bp.route('/slide/delete/<string:id>', methods=['GET', 'POST'])
def delete_slider(id):
    try:
        if request.method == "POST":
            resource_type = request.values.get('type')
            delete_result = ""
            if resource_type == 'video':
                delete_result = cloudinary.uploader.destroy(
                    id, resource_type="video")
            elif resource_type == "link":
                YoutubeVideos.query.filter_by(id=id).delete()
                db.session.commit()
                return jsonify({'status': 'success', 'message': 'deleted successfully'})
            else:
                delete_result = cloudinary.uploader.destroy(id)
            if delete_result['result'] == 'ok':
                slider_type = request.values.get('type')
                if slider_type == 'image':
                    HeroSlider.query.filter_by(public_id=id).delete()
                    db.session.commit()
                    return jsonify({'status': 'success', 'message': 'Slider deleted successfully'})
                elif slider_type == 'about':
                    AboutImges.query.filter_by(public_id=id).delete()
                    db.session.commit()
                    return jsonify({'status': 'success', 'message': 'Slider deleted successfully'})
                elif slider_type == 'logo':
                    Clients.query.filter_by(public_id=id).delete()
                    db.session.commit()
                    return jsonify({'status': 'success', 'message': 'Slider deleted successfully'})
                elif slider_type == 'video':
                    HeroVideos.query.filter_by(public_id=id).delete()
                    db.session.commit()
                    return jsonify({'status': 'success', 'message': 'Slider deleted successfully'})
                else:
                    return jsonify({'status': 'error', 'message': 'Failed to delete item'})
            else:
                return jsonify({'status': 'error', 'message': 'Failed to delete item'})
    except cloudinary.exceptions.Error as e:
        return jsonify({'status': 'error', 'message': 'Failed to delete item'})
    return redirect(request.url)
