import logging
import os

os.makedirs("logs", exist_ok=True)

log_file_path = os.path.join("logs", "automation.log")

logger = logging.getLogger("automation_logger")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler(log_file_path)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def log_message(message, level="info"):
    if level == "error":
        logger.error(message)
    else:
        logger.info(message)
