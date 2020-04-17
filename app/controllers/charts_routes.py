from flask import render_template
from app import app
from app.controllers.data_processing import DataProcessing as Dp
from app.models.charts_sql import Database
import datetime
db = Database()


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/home/')
def home():
    open_order = Dp(db.open_order_sql())
    open_order = open_order.open_orders()
    open_bill = Dp(db.open_bills_sql())
    open_bill = open_bill.open_bills()
    top_seller = Dp(db.top_seller_sql())
    top_seller = top_seller.top_sellers()
    last_30_month = Dp(db.last_30_months_sql())
    last_30_month = last_30_month.last_30_months()

    return render_template('index.html', open_order=open_order, open_bill=open_bill, top_seller=top_seller,
                           last_30_month=last_30_month)


@app.route('/landing/')
def landing():
    return render_template('landing-page.html')
