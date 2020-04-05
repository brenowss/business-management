from flask import render_template
from app import app
from app.controllers.data_processing import open_orders, open_bills


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/home/')
def home():
    open_order = open_orders()
    open_bill = open_bills()
    return render_template('index.html', open_order=open_order, open_bill=open_bill)


@app.route('/landing')
def landing():
    return render_template('landing-page.html')
