from flask import Blueprint, jsonify, render_template, redirect, url_for, session, request, flash
from werkzeug.utils import secure_filename
from app import db
from app.models.model import Product,ProductCategory
from app.utils import allowed_file
import os
import cloudinary.uploader # type: ignore

product_bp = Blueprint('product',__name__)

@product_bp.route("/product")
def product():
    products = Product.query.all()
    category = ProductCategory.query.all()
    print(category)
    return render_template('admin/products.html',data={
        "categories":category,
        "products":products
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
        name = request.form.get('name')
        category = request.form.get('category')
        colors = request.form.get('color')
        price = request.form.get('original_price')
        discount_percent = request.form.get('discount_price')
        weight = request.form.get('weight')
        description = request.form.get('description')

        image_file = request.files.getlist('image')
        upload_results = []

        if image_file:
            for image in image_file:
                result = cloudinary.uploader.upload(image)
                upload_results.append({
                                      "image_url":result["secure_url"],
                                      "public_id":result["public_id"]}
            )
               
            new_product = Product(name=name, price=price,
                                  images=upload_results, description=description,discount_percent=discount_percent,weight=weight,colors=colors)
            if category:
                new_product.categories.append(ProductCategory.query.get(category))

            print(upload_results)
            print("-----l----")

            db.session.add(new_product)
            db.session.commit()
            flash('Product added successfully.', 'success')
            return redirect(url_for('admin.admin'))
        else:
            flash('No image selected or invalid file type.', 'error')
            return redirect(request.url)
    else:
        category = ProductCategory.query.all()
       
        return render_template("admin/add-product.html",data={
        "categories":category, })


@product_bp.route('/admin/edite_product/<int:product_id>', methods=['GET', 'POST'])
def edite_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        # Get form data and convert to dictionary
        form_data = {
            'name': request.form.get('name'),
            'category': request.form.get('category'),
            'colors': request.form.get('color'),
            'price': request.form.get('original_price'),
            'discount_percent': request.form.get('discount_price'),
            'weight': request.form.get('weight'),
            'description': request.form.get('description')
        }

        # Iterate over form data and update only changed fields
        for key, value in form_data.items():
            if value and value != str(getattr(product, key)):
                setattr(product, key, value)

        # Handle categories separately if necessary
        if form_data['category']:
            category = ProductCategory.query.get(form_data['category'])
            if category and category not in product.categories:
                product.categories = [category]

        # Handle image uploads
        image_files = request.files.getlist('image')
        if image_files:
            upload_results = []
            for image in image_files:
                result = cloudinary.uploader.upload(image)
                upload_results.append({
                    "image_url": result["secure_url"],
                    "public_id": result["public_id"]
                })
            if upload_results:
                product.images = upload_results

        try:
            db.session.commit()
            flash('Product updated successfully.', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating product: {str(e)}', 'error')

        return redirect(url_for('admin.admin'))
    else:
        category = ProductCategory.query.all()
        return render_template("admin/edit-product.html", product=product,categories=category)


@product_bp.route('/admin/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)

    try:
        # Delete images from Cloudinary
        if product.images:
            for image in product.images:
                cloudinary.uploader.destroy(image['public_id'])

        # Delete the product from the database
        db.session.delete(product)
        db.session.commit()

        flash('Product deleted successfully.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting product: {str(e)}', 'error')

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
        