import os 
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from controllers import login_controller, product_list_controller, product_controller, category_controller, auth_controller 

app.register_blueprint(login_controller.bp)
app.register_blueprint(product_list_controller.bp)
app.register_blueprint(product_controller.bp)
app.register_blueprint(category_controller.bp)
app.register_blueprint(auth_controller.bp)   

app = Flask(__name__)
app.config('SQLALCHEMY_DATABASE_URI') = 'sqlite.///db.sqlite3'
db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    products = db.relationship('Product', backref = 'category', lazy = True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    manufacture_date = db.Column(db.String(20))
    expiry_date= db.Column(db.String(20))
    rate_per_unit = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = False)

@app.route('/')
def index():
    categories = Category.query.all()
    return render_template('index.html.jinja2', categories = categories)

@app.route('/add_category', methods = ['POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        category = Category(name = name)
        db.session.add(category)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_product', methods = ['POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        manufacture_date = request.form['manufacture_date']
        expiry_date = request.form['expiry_date']
        rate_per_unit = float(request.form['rate_per_unit'])
        category_id = int(request.form['category_id'])
        product = Product(name = name, manufacture_date = manufacture_date, expiry_date = expiry_date, 
                          rate_per_unit = rate_per_unit, category_id = category_id)
        db.session.add(product)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(host = "0.0.0.0", debug = True)


