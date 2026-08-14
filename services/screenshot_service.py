import os
from datetime import datetime


def save_screenshot(driver, patient_id):
    os.makedirs("screenshots", exist_ok=True)

    filename = f"screenshots/{patient_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    driver.save_screenshot(filename)

    return filename
