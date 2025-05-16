from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
from app.back.logic.inventory_service import InventoryService
from app.back.db.sqlite_cache import SQLiteCache

class InventoryView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.db      = SQLiteCache()
        self.service = InventoryService(self.db)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("📦 Inventario"))
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Producto","Categoría","Cantidad","Precio"])
        layout.addWidget(self.table)
        btn_refresh = QPushButton("🔄 Refrescar")
        btn_refresh.clicked.connect(self.load_stock)
        layout.addWidget(btn_refresh)
        self.setLayout(layout)
        self.load_stock()

    def load_stock(self):
        self.table.setRowCount(0)
        for prod in self.service.get_stock():
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(prod['nombre']))
            self.table.setItem(row, 1, QTableWidgetItem(prod['categoria']))
            self.table.setItem(row, 2, QTableWidgetItem(str(prod['cantidad'])))
            self.table.setItem(row, 3, QTableWidgetItem(str(prod['precio_unitario'])))
