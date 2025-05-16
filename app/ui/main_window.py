from PySide6.QtWidgets import QMainWindow, QStackedWidget
from app.ui.dashboard_view import DashboardView
from app.ui.invoice_view import InvoiceView
from app.ui.accounting_view import AccountingView
from app.ui.inventory_view import InventoryView
from app.ui.client_view import ClientView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin PyME")
        self.resize(1024, 768)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self._init_views()

    def _init_views(self):
        self.dashboard = DashboardView()
        self.invoices  = InvoiceView()
        self.accounting= AccountingView()
        self.inventory = InventoryView()
        self.clients   = ClientView()
        for view in [self.dashboard, self.invoices, self.accounting, self.inventory, self.clients]:
            self.stack.addWidget(view)
