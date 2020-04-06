from app.models import Database


class DataProcessing:

    db = Database()

    def __init__(self, data):
        self.data = data

    def open_orders(self):
        for i in self.data:
            i['vlr_aberto'] = int(i['vlr_aberto'])
        self.data = sorted(self.data, key=lambda data: data['vlr_aberto'])
        self.data = self.data[len(self.data) - 20:]
        return self.data

    def open_bills(self):
        for i in self.data:
            i['vlt_total'] = int(i['vlt_total'])
        for i in self.data:
            b = str(i['data_docto'])
            b = b.replace('-', ' ')
            i['data_docto'] = tuple(b.split())
        return self.data

    def top_sellers(self):
        for i in self.data:
            i['vlr_vendedor'] = int(i['vlr_vendedor'])
        return self.data


