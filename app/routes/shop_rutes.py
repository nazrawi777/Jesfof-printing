from flask import Blueprint, jsonify , render_template, session
from app.models.model import Product

shop_bp = Blueprint('shop',__name__)


@shop_bp.route('/shop')
def shop():
    products = Product.query.all()
    session["user"] = 'Current user'
    session["cart"] = []
    return render_template('shop.html',data={
        "products":products
    })


@shop_bp.route('/shop-details/<int:product_id>')
def shop_details(product_id):
    product = Product.query.get(product_id)
    print(product.discount_percent)
    print(product.price)   
    return render_template('shopdetails.html', product=product)


@shop_bp.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    try:
        # Retrieve product from database
        product = Product.query.filter_by(id=product_id).first()
        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Serialize product information
        product_data = {
            "id": product.id,
            "image_url": product.images[0],
            "name": product.name,
            "price": product.price,
            "quantity": 1  
        }

        cart_items = session.get("cart", [])
        cart_items.append(product_data)
        session["cart"] = cart_items

        return jsonify({"success": "Product added successfully", "cart": session["cart"]})
    except Exception as e:
        print(e)
        return jsonify({"error": "Failed to add product to cart"}), 500




@shop_bp.route('/get/cart-items', methods=['GET'])
def get_shop_cart():
    try:
        # Retrieve cart items from session, if it exists
        cart_items = session.get("cart", [])
        return jsonify({"cart": cart_items})
    except Exception as e:
        print(e)
        return jsonify({"error": "Failed to retrieve cart"}), 500


