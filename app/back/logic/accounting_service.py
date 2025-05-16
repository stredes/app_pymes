class AccountingService:
    def __init__(self, db):
        self.conn = db.get_connection()

    def create_entry(self, entry):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO LibroDiario(id_asiento, fecha, cuenta, debe, haber, glosa) VALUES (?, ?, ?, ?, ?, ?)",
            (
                entry['id_asiento'], entry['fecha'], entry['cuenta'],
                entry['debe'], entry['haber'], entry.get('glosa', '')
            )
        )
        self.conn.commit()

    def get_entries(self, filters=None):
        cur = self.conn.cursor()
        sql = "SELECT id_asiento, fecha, cuenta, debe, haber FROM LibroDiario"
        if filters:
            sql += " WHERE " + filters
        cur.execute(sql)
        return [
            dict(id_asiento=r[0], fecha=r[1], cuenta=r[2],
                 debe=r[3], haber=r[4])
            for r in cur.fetchall()
        ]

    def get_balance_sheet(self):
        cur = self.conn.cursor()
        cur.execute(
            "SELECT cuenta, SUM(debe)-SUM(haber) AS saldo FROM LibroDiario GROUP BY cuenta"
        )
        return {r[0]: r[1] for r in cur.fetchall()}
