import sqlite3
from config.settings import DB_PATH


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS charges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            cpt_code TEXT,
            charge_amount TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()
