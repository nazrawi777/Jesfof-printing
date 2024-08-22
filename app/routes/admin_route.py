from flask import Blueprint, render_template, redirect, url_for, session, request, flash

from app.models.model import User


admin_bp = Blueprint("admin",__name__)

@admin_bp.route("/admin")
def admin():
  """if 'admin_logged_in' not in session or not session['admin_logged_in']:
        return render_template('admin/login.html')"""
  image_url =  'blog-2.jpg'
  return render_template("admin/new_admin.html", data={
      "products":[],
      "slidImg":[],
      "slideVideo":[],
      "links":[],
      "linclient_list":[],
      "about_img":[], 
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



