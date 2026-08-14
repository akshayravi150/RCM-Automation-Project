from automation.login_bot import login_test
from automation.rcm_processor import process_rcm_data

if __name__ == "__main__":

    driver = login_test()

    if driver is None:
        print("Login Failed. Bot Stopped.")
    else:
        process_rcm_data(driver)
        driver.quit()
