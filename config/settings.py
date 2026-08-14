import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV = "dev"  # change to prod later

config_file = f"config_{ENV}.json"
config_path = os.path.join(BASE_DIR, "config", config_file)

with open(config_path) as f:
    config = json.load(f)

DB_PATH = os.path.join(BASE_DIR, config.get("db_path", "db/rcm_data.db"))
LOGIN_URL = config.get("login_url", "http://127.0.0.1:5000/login")
EXCEL_PATH = os.path.abspath(os.path.join(BASE_DIR, config.get("excel_path", "data/charges.xlsx")))
HEADLESS = config.get("headless", False)
TIMEOUT = config.get("timeout", 20)
TENANT_ID = config.get("tenant_id", "default")
