from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from werkzeug.utils import secure_filename
from app import db
from app.models.model import Product,ProductCategory
from app.utils import allowed_file
import os
import cloudinary.uploader # type: ignore

product_bp = Blueprint('product',__name__)

@product_bp.route("/product")
def product():
    #products = Product.query.all()
    category = ProductCategory.query.all()
    print(category)
    return render_template('admin/products.html',data={
        "categories":category
    })

@product_bp.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    related_products = Product.query.filter(
        Product.id != product.id,
        Product.name.like(f'%{product.name.split()[0]}%')
    ).limit(4).all()
    return render_template('product_detail.html', product=product, related_products=related_products)


@product_bp.route("/admin/add_product" ,  methods=["GET","POST"])
def add_product():
    if request.method == 'POST':
        print("-----l----")
        print(request.files.get("image"))
        print(request.form.get("name"))
        name = request.form.get('name')
        category = request.form.get('category')
        colors = request.form.get('color')
        price = request.form.get('original_price')
        discount_percent = request.form.get('discount_price')
        weight = request.form.get('weight')
        description = request.form.get('description')
        image_file = request.files.get('image')
        print("Made It to HEre ")
        if image_file and allowed_file(image_file.filename):
            print("Made It to HEre ")
            # Upload image to Cloudinary
            upload_result = cloudinary.uploader.upload(
                image_file, resource_type='auto')
            
            new_product = Product(name=name, price=price,
                                  images=[{
                                      "image_url":upload_result["secure_url"],
                                      "public_id":upload_result["public_id"]
                                  }], description=description,discount_percent=discount_percent,weight=weight,colors=colors)
            if category:
                new_product.categories.append(ProductCategory.query.get(category))

            db.session.add(new_product)
            db.session.commit()
            flash('Product added successfully.', 'success')
            return redirect(url_for('admin.admin'))
        else:
            flash('No image selected or invalid file type.', 'error')
            return redirect(request.url)
    else:
        category = ProductCategory.query.all()
        products = Product.query.all()
        return render_template("admin/add-product.html",data={
        "categories":category})


@product_bp.route('/admin/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edite_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form.get('name')
        product.price = request.form.get('price')
        product.description = request.form.get('description')
        image_file = request.files.get('image')
        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(os.getenv('UPLOAD_FOLDER'), filename)
            image_file.save(image_path)
            product.image = filename
        db.session.commit()
        product.log_action('Edited',f"Product '{product.name}' edited successfully.")
        flash('Product updated successfully.', 'success')
        return redirect(url_for('admin.admin'))


@product_bp.route('/admin/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    if 'admin_logged_in' not in session or not session['admin_logged_in']:
        return redirect(url_for('admin.login'))
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    product.log_action('Deleted',f"Product '{product.name}' deleted successfully")
    flash('Product deleted successfully.', 'success')
    return redirect(url_for('admin.admin'))



@product_bp.route("/admin/add_product_category" , methods=["GET","POST"])
def add_product_category():
    if request.method == 'POST':
        category_name = request.form.get('category_name')
        if category_name:
            new_category = ProductCategory(category_name=category_name)
            db.session.add(new_category)
            db.session.commit()
            flash('New Category added successfully.', 'success')
            return redirect(url_for('product.product'))
        else:
            flash('No image selected or invalid file type.', 'error')
            return redirect(url_for('product.product'))