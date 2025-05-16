from datetime import date
import xml.etree.ElementTree as ET

class InvoiceService:
    def __init__(self, db):
        self.conn = db.get_connection()

    def create_invoice(self, data):
        cursor = self.conn.cursor()
        numero = data['numero']
        fecha  = data.get('fecha', date.today())
        cid    = data['cliente_id']
        neto   = data['monto_neto']
        iva    = round(neto * 0.19, 2)
        total  = neto + iva
        estado = data.get('estado', 'PENDIENTE')

        cursor.execute(
            "INSERT INTO Facturas(numero, fecha, cliente_id, monto_neto, iva, monto_total, estado) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (numero, fecha, cid, neto, iva, total, estado)
        )
        self.conn.commit()

        root = ET.Element('Factura')
        ET.SubElement(root, 'Numero').text    = str(numero)
        ET.SubElement(root, 'Fecha').text     = str(fecha)
        ET.SubElement(root, 'ClienteID').text = str(cid)
        ET.SubElement(root, 'MontoNeto').text = str(neto)
        ET.SubElement(root, 'IVA').text       = str(iva)
        ET.SubElement(root, 'Total').text     = str(total)
        return ET.tostring(root, encoding='utf-8', method='xml')

    def get_invoices(self, filters=None):
        cursor = self.conn.cursor()
        sql = "SELECT numero, fecha, cliente_id, monto_total, estado FROM Facturas"
        if filters:
            sql += " WHERE " + filters
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [
            dict(numero=r[0], fecha=r[1], cliente_id=r[2],
                 monto_total=r[3], estado=r[4])
            for r in rows
        ]
