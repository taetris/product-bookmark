# User puts link for product
# Add product to user's blog
# Scrape data from daraz at random intervals for product
# if(price<previous_price):
#   send_alert_via_email or discord()
#

from flask import Flask, render_template, url_for, redirect, request
import sqlite3
import sys
from flask_apscheduler import APScheduler as scheduler
from scrape import scrape
from db_connect import get_db_connection
from schedule import scheduler

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


def get_product(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products').fetchone()
    conn.close()
    if product is None:
        abort(404)
    return product

# @app.route('/<int:post_id>')
# def post(post_id):
#     post = get_post(post_id)
#     return render_template('post.html', post=post)

@app.route('/', methods=('GET','POST', 'product'))
def index():
    conn, cur = get_db_connection()
    # products = conn.execute('SELECT * FROM products').fetchall()
    

    img = "static/files/default.png"
    
    print("start")
    if (request.method == 'POST'):    # submitted
        input_link = request.form["input_link"]
        # if (input_link == ""):
        #     img = "static/files/error.png"
        #     print("imgg")
        # else:
        product_name, price = scrape(input_link)
        query = "INSERT INTO products (input_link, product_name, price) VALUES (?, ?, ?)"
        params = (input_link, product_name, price)
        cur.execute(query, params)
        conn.commit()
        conn.close()

        print("added")
        return redirect(url_for('product'))
        # info_list = scrape(input_link)
        # print(info_list)
    else:
     
        return render_template("index.html", image = img)


@app.route('/product', methods = ('GET', 'POST'))
def product():
    result = "nothing"
    # if request.method == "GET":
    # prod_url = request.args.get("")
    conn, cur = get_db_connection()
    cur.execute("SELECT * FROM products")
    result = cur.fetchall()
    conn.close()
    return render_template('product.html', result = result)

@app.route('/inventory', methods = ('GET', 'POST'))
def inventory():
    return render_template('inventory.html')