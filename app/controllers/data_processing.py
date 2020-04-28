from app.models.charts_sql import Database
import pandas as pd
from pprint import pprint


def date_format(data):
    for i in data:
        b = str(i['data_docto'])
        b = b.replace('-', ' ')
        i['data_docto'] = tuple(b.split())
    return data


def decimal_format(data):
    for i in data:
        i['vlt_total'] = int(i['vlt_total'])
    return data


def order_by_vlt_total(data):
    data = sorted(data, key=lambda f_data: f_data['vlt_total'])
    return data


class DataProcessing:

    db = Database()

    def __init__(self, data):
        self.data = data

    def open_orders(self):
        decimal_format(self.data)
        df = pd.DataFrame(self.data)
        self.data = df.groupby(['cod_cliente', 'nm_cliente'], as_index=False).sum()
        self.data = self.data.to_dict('records')
        self.data = order_by_vlt_total(self.data)
        self.data = self.data[len(self.data) - 20:]
        return self.data

    def open_bills(self):
        date_format(self.data)
        decimal_format(self.data)
        df = pd.DataFrame(self.data)
        self.data = df.groupby(['num_documento', 'data_docto'], as_index=False).sum()
        self.data = self.data.to_dict('records')
        return self.data

    def top_sellers(self):
        decimal_format(self.data)
        df = pd.DataFrame(self.data)
        self.data = df.groupby(['nm_representante', 'cod_vendedor'], as_index=False).sum()
        self.data = self.data.to_dict('records')
        self.data = order_by_vlt_total(self.data)
        return self.data

    def last_30_months(self):
        date_format(self.data)
        decimal_format(self.data)
        return self.data

