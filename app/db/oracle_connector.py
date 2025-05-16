import os
import cx_Oracle
from dotenv import load_dotenv

load_dotenv()
WALLET_DIR = os.getenv("ORACLE_WALLET_DIR")
USER       = os.getenv("ORACLE_USER")
PASSWORD   = os.getenv("ORACLE_PASSWORD")
DSN        = os.getenv("ORACLE_DSN")

class OracleConnector:
    def __init__(self):
        cx_Oracle.init_oracle_client(lib_dir=WALLET_DIR)
        self.conn = cx_Oracle.connect(user=USER, password=PASSWORD, dsn=DSN)

    def get_connection(self):
        return self.conn
