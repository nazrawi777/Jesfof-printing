from  .main import main_bp
from .shop_rutes import shop_bp


def register_blue_prints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(shop_bp)