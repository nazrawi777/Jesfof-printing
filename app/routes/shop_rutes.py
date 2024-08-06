from flask import Blueprint , render_template

shop_bp = Blueprint('shop',__name__)


@shop_bp.route('/shop')
def shop():
    return render_template('shop.html')


@shop_bp.route('/shop-details')
def shop_details():
    return render_template('shop-details.html')