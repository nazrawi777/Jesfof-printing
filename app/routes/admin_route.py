from flask import Blueprint, render_template, redirect, url_for, session, request, flash

from app.models.model import User,HeroSlider,HeroVideos,YoutubeVideos,AboutImges,Clients,HeroExpandImage


admin_bp = Blueprint("admin",__name__)

@admin_bp.route("/admin")
def admin():
  """if 'admin_logged_in' not in session or not session['admin_logged_in']:
        return render_template('admin/login.html')"""
  image_url =  'blog-2.jpg'
  hero_slides = HeroSlider.query.all()
  about_imgs = AboutImges.query.all()
  client_logos = Clients.query.all()
  gallery_images = HeroExpandImage.query.all()
  videos = HeroVideos.query.all()
  youtube_links = YoutubeVideos.query.all()
  
  data={
      "banners":hero_slides,
       "about_imgs":about_imgs,
      "client_logos":client_logos,
      "gallery_images":gallery_images,
      "videos":videos,
      "youtube_videos":youtube_links,
  }

  print(data)


  return render_template("admin/new_admin.html", data={
      "banners":hero_slides,
       "about_imgs":about_imgs,
      "client_logos":client_logos,
      "gallery_images":gallery_images,
      "videos":videos,
      "youtube_videos":youtube_links,
  },image_url=image_url)

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    if not username or not password:
        flash('Please enter both username and password.', 'error')
    else:
        find_user = User.query.filter_by(username=username).first()
        if find_user and find_user.password == password:
            session['admin_logged_in'] = True
            session['username'] = username
            session['role'] = find_user.role
            return redirect(url_for('admin.admin'))
        else:
            flash('Invalid username or password.', 'error')
    return render_template('admin/login.html')


@admin_bp.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('login'))



