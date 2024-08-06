from flask import Blueprint, render_template, redirect, url_for, session, request, flash
'''from werkzeug.utils import secure_filename
from app import db
from app.models.model import Product
import os'''

product_bp = Blueprint('product',__name__)

@product_bp.routes("")
def product():
    pass

@product_bp.routes("admin/add_product" , methods=["POST"])
def add_product():
    """if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        image_file = request.files.get('image')
        if image_file and True:#allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(os.getenv('UPLOAD_FOLDER'), filename)
            image_file.save(image_path)
            new_product = Product(name=name, price=price,
                                  image=filename, description=description)
            db.session.add(new_product)
            db.session.commit()
            new_product.log_action('Added', f'''Product'{name}'added successfully.''')

            flash('Product added successfully.', 'success')
            return redirect(url_for('admin.admin'))
        else:
            flash('No image selected or invalid file type.', 'error')
            return redirect(request.url)"""

@product_bp.routes('/admin/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edite_product(product_id):
    """product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = request.form['price']
        product.description = request.form['description']
        image_file = request.files.get('image')
        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(os.getenv('UPLOAD_FOLDER'), filename)
            image_file.save(image_path)
            product.image = filename
        db.session.commit()
        product.log_action('Edited',f"Product '{product.name}' edited successfully.")
        flash('Product updated successfully.', 'success')
        return redirect(url_for('admin.admin'))"""

@product_bp.routes('/admin/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    """if 'admin_logged_in' not in session or not session['admin_logged_in']:
        return redirect(url_for('admin.login'))
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    product.log_action('Deleted',f"Product '{product.name}' deleted successfully")
    flash('Product deleted successfully.', 'success')
    return redirect(url_for('admin.admin'))"""

