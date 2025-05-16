from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem

class InvoiceView(QWidget):
    def __init__(self, invoice_service, parent=None):
        super().__init__(parent)
        self.service = invoice_service
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("📄 Facturación Electrónica"))
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(
            ["Número","Fecha","Cliente","Total","Estado"])
        layout.addWidget(self.table)
        btn = QPushButton("🔄 Refrescar")
        btn.clicked.connect(self.load_invoices)
        layout.addWidget(btn)
        self.setLayout(layout)
        self.load_invoices()

    def load_invoices(self):
        self.table.setRowCount(0)
        for inv in self.service.get_invoices():
            r = self.table.rowCount()
            self.table.insertRow(r)
            self.table.setItem(r, 0, QTableWidgetItem(str(inv['numero'])))
            self.table.setItem(r, 1, QTableWidgetItem(str(inv['fecha'])))
            self.table.setItem(r, 2, QTableWidgetItem(str(inv['cliente_id'])))
            self.table.setItem(r, 3, QTableWidgetItem(str(inv['monto_total'])))
            self.table.setItem(r, 4, QTableWidgetItem(inv['estado']))
