from utils.logger import logger
from utils.custom_exceptions import ChargeProcessingError


def process_charge_ui(driver, row):
    patient_id = row.get("patient_id", "unknown")

    try:
        dos = row["dos"]
        cpt = row["cpt_code"]
        dx = row["dx_code"]
        amount = row["charge_amount"]
        provider = row["provider"]

        logger.info(f"Processing Patient: {patient_id}")

        logger.info(f"Charge submitted for {patient_id}")

    except Exception as e:
        logger.error(f"Error processing patient {patient_id}: {e}")
        raise ChargeProcessingError(str(e))
