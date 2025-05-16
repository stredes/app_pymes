from app.db.oracle_connector import OracleConnector
from app.db.sqlite_cache import SQLiteCache

class SyncManager:
    def __init__(self):
        self.oracle = OracleConnector().get_connection()
        self.sqlite = SQLiteCache().get_connection()
        self.tables = ['Clientes','Facturas','LibroDiario','Inventario','FiltrosGuardados']

    def pull_remote(self):
        ora_cur = self.oracle.cursor()
        sql_cur = self.sqlite.cursor()
        for t in self.tables:
            ora_cur.execute(f"SELECT * FROM {t}")
            rows = ora_cur.fetchall()
            sql_cur.execute(f"DELETE FROM {t}")
            if rows:
                ph = ",".join(["?" for _ in rows[0]])
                sql_cur.executemany(f"INSERT INTO {t} VALUES ({ph})", rows)
        self.sqlite.commit()

    def push_local(self):
        ora_cur = self.oracle.cursor()
        sql_cur = self.sqlite.cursor()
        for t in self.tables:
            ora_cur.execute(f"DELETE FROM {t}")
            sql_cur.execute(f"SELECT * FROM {t}")
            rows = sql_cur.fetchall()
            if rows:
                for row in rows:
                    placeholders = ",".join(["?"] * len(row))
                    ora_cur.execute(f"INSERT INTO {t} VALUES ({placeholders})", row)
        self.oracle.commit()

    def resolve_conflicts(self):
        # Última modificación gana (pull/push sobrescribe)
        pass
