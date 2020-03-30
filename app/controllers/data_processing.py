from app.models import Database
from datetime import datetime


def open_orders():
    db = Database()
    open_order = db.open_order()
    for i in open_order:
        i['vlr_aberto'] = int(i['vlr_aberto'])
    open_order = sorted(open_order, key=lambda open_order: open_order['vlr_aberto'])
    open_order = open_order[len(open_order) - 20:]
    return open_order


def open_bills():
    db = Database()
    open_bills = db.open_bills()
    a = ()
    for i in open_bills:
        i['vlt_total'] = int(i['vlt_total'])
    for i in open_bills:

        b = str(i['data_docto'])
        b = b.replace('-', ' ')
        i['data_docto'] = tuple(b.split())
    return open_bills

