import flask, os, flask_login
from .models import *

def render_catalog():
    is_admin = False
    if flask_login.current_user.is_authenticated and flask_login.current_user.is_admin:
        is_admin = True
    if flask.request.method == "POST" and is_admin:
        new_product = Product(
            name = flask.request.form.get("name"),
            price = flask.request.form.get("price"),
            description = flask.request.form.get("description"),
            count = flask.request.form.get("count"),
            discount = flask.request.form.get("discount"),
        )
        
        DB.session.add(new_product)
        DB.session.commit()
        image = flask.request.files.get('image')
        image.save(
            dst = os.path.abspath(os.path.join(__file__, '..', 'static', 'images', "products", f'{new_product.id}.png'))
        )
    all_products = Product.query.all()
    return flask.render_template("catalog.html", admin = is_admin, products = all_products)
