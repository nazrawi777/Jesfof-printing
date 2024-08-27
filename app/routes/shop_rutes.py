from flask import Blueprint , render_template, session
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


@shop_bp.route('/add-cart/product/<int:product_id>')
def add_shop_cart(product_id):
    cart_items = session["cart"]
    cart_items.append(Product.query.filter_by(id=product_id).first())
    return render_template('shop-details.html')

