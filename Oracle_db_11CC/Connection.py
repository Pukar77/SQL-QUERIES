from pathlib import Path
import os
from dotenv import load_dotenv
import oracledb

load_dotenv(Path.cwd().parent / ".env")

def get_connection():
    return oracledb.connect(
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        dsn=os.getenv("DB_DSN")
    )
