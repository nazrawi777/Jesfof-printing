from sqlalchemy import Integer, String, Boolean, DateTime

from app import db

class HeroSlider(db.Model):
    id= db.Column(Integer,primary_key=True)
    text = db.Column(String(500),nullable=False)
    bg_image_url = db.Column(String(500),nullable=False) 

class AboutImges(db.Model):
    id= db.Column(Integer,primary_key=True)
    img_url = db.Column(String(400) )


class ServiceCard(db.Model):
    id= db.Column(Integer,primary_key=True)
    text = db.Column(String(200))
    card_img_url = db.Column(String(200))

class ProductColor(db.Model):
        id= db.Column(Integer,primary_key=True)
        color = db.Column(String(100))
        product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

class ProductCategory(db.Model):
         id= db.Column(Integer,primary_key=True)
         category_name = db.Column(String(200))
         product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)


class Product(db.Model):
    id= db.Column(Integer,primary_key=True)
    name = db.Column(String(200),nullable=False)
    price = db.Column(Integer)
    description = db.Column(String(300))
    detailed_description = db.Column(String(300))
    discount_persent = db.Column(Integer)
    weight= db.Column(Integer)
    product_categorys = db.relationship('ProductCategory', backref='product', lazy=True)
    product_colors = db.relationship('ProductColor', backref='product', lazy=True)
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(250), default="user", nullable=False)
  
