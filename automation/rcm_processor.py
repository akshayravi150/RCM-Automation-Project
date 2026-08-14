import pandas as pd
from config.settings import EXCEL_PATH
from services.ui_charge_processor import process_charge_ui
from utils.logger import logger


def process_rcm_data(driver):

    if driver is None:
        logger.error("Driver not initialized. Stopping execution.")
        return

    df = pd.read_excel(EXCEL_PATH)

    if "Status" not in df.columns:
        df["Status"] = ""

    if "Comment" not in df.columns:
        df["Comment"] = ""

    df["Status"] = df["Status"].astype(str)
    df["Comment"] = df["Comment"].astype(str)

    for index, row in df.iterrows():

        try:
            process_charge_ui(driver, row)

            df.loc[index, "Status"] = "Success"
            df.loc[index, "Comment"] = "Charge Submitted"

            logger.info(f"Row {index} processed successfully")

        except Exception as e:

            df.loc[index, "Status"] = "Failed"
            df.loc[index, "Comment"] = str(e)

            logger.error(f"Row {index} failed: {e}")

    df.to_excel(EXCEL_PATH, index=False)

    logger.info("Excel updated with status")
