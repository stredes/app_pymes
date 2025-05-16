import sqlite3

SCHEMA = [
    "CREATE TABLE IF NOT EXISTS Clientes (id_cliente INTEGER PRIMARY KEY, nombre TEXT, rut TEXT UNIQUE, direccion TEXT, telefono TEXT, email TEXT)",
    "CREATE TABLE IF NOT EXISTS Facturas (id_factura INTEGER PRIMARY KEY AUTOINCREMENT, numero TEXT UNIQUE, fecha TEXT, cliente_id INTEGER, monto_neto REAL, iva REAL, monto_total REAL, estado TEXT)",
    "CREATE TABLE IF NOT EXISTS LibroDiario (id_asiento INTEGER PRIMARY KEY, fecha TEXT, cuenta TEXT, debe REAL, haber REAL, glosa TEXT)",
    "CREATE TABLE IF NOT EXISTS Inventario (id_producto INTEGER PRIMARY KEY, nombre TEXT, categoria TEXT, cantidad INTEGER, precio_unitario REAL, codigo_barras TEXT)",
    "CREATE TABLE IF NOT EXISTS FiltrosGuardados (id_filtro INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, descripcion TEXT, modulo TEXT, condiciones_json TEXT)"
]

class SQLiteCache:
    def __init__(self, path="local_cache.db"):
        self.conn = sqlite3.connect(path)
        self._init_schema()

    def _init_schema(self):
        cur = self.conn.cursor()
        for stmt in SCHEMA:
            cur.execute(stmt)
        self.conn.commit()

    def get_connection(self):
        return self.conn
