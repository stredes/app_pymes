from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from app.back.logic.client_service import ClientService
from app.back.db.sqlite_cache import SQLiteCache

class ClientView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db      = SQLiteCache()
        self.service = ClientService(self.db)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("👥 Clientes"))
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["ID","Nombre","RUT","Email"])
        layout.addWidget(self.table)
        btn_refresh = QPushButton("🔄 Refrescar")
        btn_refresh.clicked.connect(self.load_clients)
        layout.addWidget(btn_refresh)
        self.setLayout(layout)
        self.load_clients()

    def load_clients(self):
        self.table.setRowCount(0)
        for cl in self.service.get_clients():
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(cl['id_cliente'])))
            self.table.setItem(row, 1, QTableWidgetItem(cl['nombre']))
            self.table.setItem(row, 2, QTableWidgetItem(cl['rut']))
            self.table.setItem(row, 3, QTableWidgetItem(cl['email']))
