import pymysql
from datetime import date, timedelta


class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "kerdos"
        password = "123"
        db = "kerdos"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def open_order_sql(self):
        self.cur.execute("""select sum(pi.vlt_total) as vlr_aberto, pb.cod_cliente, pb.nm_cliente
                            from pedido_base pb 
                              join ped_item pi on pi.key_pedido = pb.num_pedido
                              join clientes c on c.cod_cliente = pb.cod_cliente
                            where  pb.status_ped = 'A'
                            group by pb.cod_cliente
                            order by pi.vlt_total asc;""")
        result = self.cur.fetchall()
        return result

    def open_bills_sql(self):
        self.cur.execute("""select nb.num_documento, sum(ni.vlt_total) as vlt_total, nb.data_docto from nota_item ni join nota_base nb on 
                            nb.num_documento = ni.key_nota where nb.status_nota = 'A' and nb.data_docto IS NOT NULL 
                            group by ni.key_nota order by vlt_total;""")
        result = self.cur.fetchall()
        return result

    def top_seller_sql(self):
        self.cur.execute("""select sum(pi.vlt_total) as vlr_vendedor, rep.nm_representante
                                from pedido_base pb 
                                join ped_item pi on pi.key_pedido = pb.num_pedido
                                join representantes rep on rep.cod_representante =  pb.cod_vendedor
                            group by pb.cod_vendedor order by vlr_vendedor;""")
        result = self.cur.fetchall()
        return result

    def top_products_sql(self):
        self.cur.execute("""select sum(ni.vlt_total) as valor_produtos, ni.nm_produto
                                from nota_base nb join nota_item ni on ni.key_nota = nb.key_nota
                                where nb.status_nota = 'F'
                                group by ni.cod_produto
                                ORDER BY  sum(ni.vlt_total) DESC
                            LIMIT 10;""")
        result = self.cur.fetchall()
        return result
    
    def last_30_months_sql(self):
        a = date.today() - timedelta(days=30)
        a = str(a)
        self.cur.execute(f"""select nsi.vlt_total, data_docto 
                                from nota_item nsi join nota_base nb on nb.key_nota = nsi.key_nota 
                                where data_docto > '{a}'
                                order by data_docto;""")
        result = self.cur.fetchall()
        return result
        

