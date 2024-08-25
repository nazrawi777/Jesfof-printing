from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.types import JSON
from app import db

class HeroSlider(db.Model):
    id= db.Column(Integer,primary_key=True)
    sub_title = db.Column(String(500),nullable=False)
    title = db.Column(String(500),nullable=False)
    body = db.Column(String(500),nullable=False)
    btn_text = db.Column(String(500),nullable=False)
    public_id = db.Column(String(200),nullable=False)
    bg_image_url = db.Column(String(500),nullable=False)


class Clients(db.Model):
     id= db.Column(Integer,primary_key=True)
     public_id = db.Column(String(200),nullable=False)
     image_url = db.Column(String(500),nullable=False)

class HeroVideos(db.Model):
     id= db.Column(Integer,primary_key=True)
     public_id = db.Column(String(200),nullable=False)
     video_url = db.Column(String(500),nullable=False)

class YoutubeVideos(db.Model):
     id= db.Column(Integer,primary_key=True)
     youtube_url = db.Column(String(300),nullable=False)     

class AboutImges(db.Model):
    id= db.Column(Integer,primary_key=True)
    public_id = db.Column(String(200),nullable=False)
    img_url = db.Column(String(400),nullable=False)

class AboutText(db.Model):
     id= db.Column(Integer,primary_key=True)
     about_text= db.Column(String(800),nullable=False)

class HeroExpandImage(db.Model):
     id= db.Column(Integer,primary_key=True)
     public_id = db.Column(String(200),nullable=False)
     img_url = db.Column(String(500),nullable=False)

class ServiceCard(db.Model):
    id= db.Column(Integer,primary_key=True)
    text = db.Column(String(200))
    public_id = db.Column(String(200),nullable=False)
    card_img_url = db.Column(String(200))

class ProductColor(db.Model):
        id= db.Column(Integer,primary_key=True)
        color = db.Column(String(100))


# Association table to map products to categories
product_category_association = db.Table('product_category_association',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('product_category.id'), primary_key=True)
)

class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(200), nullable=False)

    # Reverse relationship to access products linked to a category
    products = db.relationship('Product', secondary=product_category_association, back_populates='categories')


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    images= db.Column(JSON, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer)
    description = db.Column(db.String(300))
    detailed_description = db.Column(db.String(300))
    discount_percent = db.Column(db.Integer)
    weight = db.Column(db.Integer)

    # Colors stored as a JSON array
    colors = db.Column(db.String(300), nullable=False)

    # Relationship to access categories linked to a product
    categories = db.relationship('ProductCategory', secondary=product_category_association, back_populates='products')

    
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(250), default="user", nullable=False)
  
