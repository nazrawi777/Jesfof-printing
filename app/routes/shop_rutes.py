from flask import Blueprint , render_template
from app.models.model import Product

shop_bp = Blueprint('shop',__name__)


@shop_bp.route('/shop')
def shop():
    products = Product.query.all()
    print(products)
    return render_template('shop.html',data={
        "products":products
    })


@shop_bp.route('/shop-details')
def shop_details():
    return render_template('shop-details.html')



@shop_bp.route('/add-cart')
def shop_details():
    
    return render_template('shop-details.html')

