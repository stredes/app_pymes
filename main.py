#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from PySide6.QtWidgets import QApplication
from app.front.ui.main_window import MainWindow
from app.front.utils.os_router import OSRouter
from app.back.db.sqlite_cache import SQLiteCache
from app.back.db.oracle_connector import OracleConnector
from app.back.db.sync_manager import SyncManager
from app.back.logic.invoice_service import InvoiceService
from app.back.logic.accounting_service import AccountingService
from app.back.logic.inventory_service import InventoryService
from app.back.logic.client_service import ClientService

def main():
    # Carga variables de entorno
    load_dotenv()

    # Detectar SO y crear data_dir
    router = OSRouter()
    data_dir = router.get_data_dir()
    data_dir.mkdir(parents=True, exist_ok=True)

    # Inicializar conexiones DB
    sqlite = SQLiteCache(path=str(data_dir/"local_cache.db"))
    ora_conn = OracleConnector().get_connection()

    # Sincronizar al arrancar
    sync = SyncManager(oracle_conn=ora_conn, sqlite_conn=sqlite.get_connection())
    sync.pull_remote()

    # Crear servicios pasando la conexión
    invoice_svc    = InvoiceService(sqlite)
    accounting_svc = AccountingService(sqlite)
    inventory_svc  = InventoryService(sqlite)
    client_svc     = ClientService(sqlite)

    # Arrancar UI
    app = QApplication([])
    window = MainWindow(
        invoice_service=invoice_svc,
        accounting_service=accounting_svc,
        inventory_service=inventory_svc,
        client_service=client_svc,
        os_router=router
    )
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
