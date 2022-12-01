# User puts link for product
# Add product to user's blog
# Scrape data from daraz at random intervals for product
# if(price<previous_price):
#   send_alert_via_email or discord()
#

from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# if request.method == "GET":
#     f"<h1>{input}</h1>"
