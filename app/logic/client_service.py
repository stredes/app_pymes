class ClientService:
    def __init__(self, db):
        self.conn = db.get_connection()

    def add_client(self, client):
        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM Clientes")
        count = cur.fetchone()[0]
        if count >= 6:
            raise Exception("Máximo 6 clientes activos alcanzado.")
        cur.execute(
            "INSERT INTO Clientes(id_cliente, nombre, rut, direccion, telefono, email) VALUES (?, ?, ?, ?, ?, ?)",
            (
                client['id_cliente'], client['nombre'], client['rut'],
                client.get('direccion',''), client.get('telefono',''),
                client.get('email','')
            )
        )
        self.conn.commit()

    def get_clients(self, filters=None):
        cur = self.conn.cursor()
        sql = "SELECT id_cliente, nombre, rut, email FROM Clientes"
        if filters:
            sql += " WHERE " + filters
        cur.execute(sql)
        return [
            dict(
                id_cliente=r[0], nombre=r[1],
                rut=r[2], email=r[3]
            )
            for r in cur.fetchall()
        ]
