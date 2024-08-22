from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from werkzeug.utils import secure_filename
from app.models.model import ServiceCard
import os

service_bp = Blueprint('service',__name__)

@service_bp.route("/services")
def services():
    return render_template("service-detail.html")

@service_bp.route("")
def add_card():
    """if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        image_file = request.files.get('image')
        if image_file and True:#allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(os.getenv('UPLOAD_FOLDER'), filename)
            image_file.save(image_path)
            new_serviceCard = ServiceCard(name=name, price=price,
                                  image=filename, description=description)
            db.session.add(new_serviceCard)
            db.session.commit()
            new_serviceCard.log_action('Added', f'''serviceCard'{name}'added successfully.''')

            flash('serviceCard added successfully.', 'success')
            return redirect(url_for('admin.admin'))
        else:
            flash('No image selected or invalid file type.', 'error')
            return redirect(request.url)"""

@service_bp.route("/services/<int:card_id>")
def delete_card(card_id):
    """if 'admin_logged_in' not in session or not session['admin_logged_in']:
        return redirect(url_for('admin.login'))
    product = ServiceCard.query.get_or_404(card_id)
    db.session.delete(product)
    db.session.commit()
    product.log_action('Deleted',f"Product '{product.name}' deleted successfully")
    flash('Product deleted successfully.', 'success')
    return redirect(url_for('admin.admin'))"""

@service_bp.route("")
def update_card():
    pass

