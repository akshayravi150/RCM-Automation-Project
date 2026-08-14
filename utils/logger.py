import logging
import os
from logging.handlers import RotatingFileHandler

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("RCM_BOT")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

file_handler = RotatingFileHandler("logs/automation.log", maxBytes=1000000, backupCount=5)
file_handler.setFormatter(formatter)

error_handler = RotatingFileHandler("logs/error.log", maxBytes=1000000, backupCount=5)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(error_handler)
