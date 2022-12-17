# User puts link for product
# Add product to user's blog
# Scrape data from daraz at random intervals for product
# if(price<previous_price):
#   send_alert_via_email or discord()
#

from flask import Flask, render_template, url_for, redirect, request
import sqlite3
from flask_apscheduler import APScheduler as scheduler
from flask_sqlalchemy import SQLAlchemy
# from scrape import scrape
app = Flask(__name__)

def scrapy():
    print("runningg...")

if __name__ == "__main__":
    scheduler.add_job(id = 'the task scheduled', func = scrapy, trigger = 'interval', seconds =5)
    scheduler.start()
    app.run('127.0.0.1', port =5000)
 

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_product(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?',
                        (product_id,)).fetchone()
    conn.close()
    if product is None:
        abort(404)
    return product

# @app.route('/<int:post_id>')
# def post(post_id):
#     post = get_post(post_id)
#     return render_template('post.html', post=post)

@app.route('/', methods=('GET', 'product'))
def index():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()

    img = "static/files/default.png"
    if request.method == 'POST':    # submitted
        input_link = request.form["url-input"]
        print(input_link)
        info_list = scrape(input_link)
        print(info_list)
        if (input_link == ""):
            img = "static/files/error.png"
           
    return render_template("index.html", image = img)


@app.route('/product', methods = ('GET', 'POST'))
def product():
    return render_template('product.html')

@app.route('/inventory', methods = ('GET', 'POST'))
def inventory():
    return render_template('inventory.html')