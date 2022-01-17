import flask
from app import forms, db
from app import app as appli
from flask import *
from app import models
from datetime import *


@appli.route("/")
def index():
    return render_template('index.html')

@appli.route("/product")
def product():
    return render_template('product.html')

@appli.route("/product/description/<id>")
def get_description(id):
    return render_template('description.html')

@appli.route("/cart")
def index():
    my_cart = models.cart.query.all()
    return render_template('cart.html')