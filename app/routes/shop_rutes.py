from flask import Blueprint, jsonify , render_template, request, session
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
    related_products = Product.query.filter(
        Product.categories.contains(product.categories[0]),
        Product.id != product.id
    ).all()
    return render_template('shopdetails.html', product=product,related_products=related_products)


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
        
        item_exists = False
        
        for item in cart_items:
            if int(item['id']) == int(product_id):
                item['quantity'] += 1
                item_exists = True
                break
    
        if not item_exists:
            #product_data['quantity'] = 1
            cart_items.append(product_data)
            
        session["cart"] = cart_items

        return jsonify({"success": "Product added successfully"})
    except Exception as e:
        print(e)
        return jsonify({"error": "Failed to add product to cart"}), 500




@shop_bp.route('/get/cart-items', methods=['GET'])
def get_shop_cart():
    try:
        # Retrieve cart items from session, if it exists
        cart_items = session.get("cart", [])
        total_cost = sum(item['price'] * item['quantity'] for item in cart_items)
        total_quantity = sum(item['quantity'] for item in cart_items)
        
        return jsonify({"cart": cart_items, "total":total_cost , "quantity": total_quantity})
    except Exception as e:
        print(e)
        return jsonify({"error": "Failed to retrieve cart"}), 500


@shop_bp.route('/delete_cart_item', methods=['POST'])
def delete_cart_item():
    try:
        product_id = request.json.get("product_id")
       
        cart_items = session.get("cart", [])
        cart_items = [item for item in cart_items if int(item['id']) != int(product_id)]
        session["cart"] = cart_items
        return jsonify({"success": "Item removed from cart"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "Failed to remove item from cart"}), 500