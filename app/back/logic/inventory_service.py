class InventoryService:
    def __init__(self, db):
        self.conn = db.get_connection()

    def add_product(self, prod):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO Inventario(id_producto, nombre, categoria, cantidad, precio_unitario, codigo_barras) VALUES (?, ?, ?, ?, ?, ?)",
            (
                prod['id_producto'], prod['nombre'], prod['categoria'],
                prod['cantidad'], prod['precio_unitario'], prod.get('codigo_barras', '')
            )
        )
        self.conn.commit()

    def update_stock(self, product_id, quantity):
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE Inventario SET cantidad = ? WHERE id_producto = ?",
            (quantity, product_id)
        )
        self.conn.commit()

    def get_stock(self, filters=None):
        cur = self.conn.cursor()
        sql = "SELECT id_producto, nombre, categoria, cantidad, precio_unitario FROM Inventario"
        if filters:
            sql += " WHERE " + filters
        cur.execute(sql)
        return [
            dict(
                id_producto=r[0], nombre=r[1], categoria=r[2],
                cantidad=r[3], precio_unitario=r[4]
            )
            for r in cur.fetchall()
        ]
