from  .main import main_bp
from .shop_rutes import shop_bp
from .admin_route import admin_bp
from .product_route import product_bp


def register_blue_prints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(product_bp)