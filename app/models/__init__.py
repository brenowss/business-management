import pymysql


class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "123"
        db = "kerdos"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def open_order(self):
        self.cur.execute("""select sum(pi.vlt_total) as vlr_aberto, pb.cod_cliente, pb.nm_cliente
                            from pedido_base pb 
                              join ped_item pi on pi.key_pedido = pb.num_pedido
                              join clientes c on c.cod_cliente = pb.cod_cliente
                            where  pb.status_ped = 'A'
                            group by pb.cod_cliente
                            order by pi.vlt_total asc;""")
        result = self.cur.fetchall()
        return result

    def open_bills(self):
        self.cur.execute("""select ni.vlt_total, nb.data_docto from nota_item ni join nota_base nb on 
                            nb.num_documento = ni.key_nota where nb.status_nota = 'A' and nb.data_docto IS NOT NULL 
                            order by vlt_total;""")
        result = self.cur.fetchall()
        return result
