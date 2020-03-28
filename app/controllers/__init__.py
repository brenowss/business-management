from flask import render_template
from app import app
from app.models import Database


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/home/')
def home():
    db = Database()
    open_order = db.open_order()
    for i in open_order:
        i['vlr_aberto'] = int(i['vlr_aberto'])
    open_order = sorted(open_order, key=lambda open_order: open_order['vlr_aberto'])
    open = open_order[len(open_order)-20:]
    return render_template('index.html', open = open)

