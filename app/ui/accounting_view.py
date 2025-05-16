from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from app.logic.accounting_service import AccountingService
from app.db.sqlite_cache import SQLiteCache

class AccountingView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db      = SQLiteCache()
        self.service = AccountingService(self.db)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("📊 Contabilidad: Libro Diario"))
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["Asiento","Fecha","Cuenta","Debe","Haber"])
        layout.addWidget(self.table)
        btn_refresh = QPushButton("🔄 Refrescar")
        btn_refresh.clicked.connect(self.load_entries)
        layout.addWidget(btn_refresh)
        self.setLayout(layout)
        self.load_entries()

    def load_entries(self):
        self.table.setRowCount(0)
        for ent in self.service.get_entries():
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(ent['id_asiento'])))
            self.table.setItem(row, 1, QTableWidgetItem(str(ent['fecha'])))
            self.table.setItem(row, 2, QTableWidgetItem(ent['cuenta']))
            self.table.setItem(row, 3, QTableWidgetItem(str(ent['debe'])))
            self.table.setItem(row, 4, QTableWidgetItem(str(ent['haber'])))
