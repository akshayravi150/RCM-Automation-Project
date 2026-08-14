from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import LOGIN_URL, HEADLESS, TIMEOUT
from utils.logger import logger


def login_test():
    try:
        options = Options()

        if HEADLESS:
            options.add_argument("--headless=new")

        service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        driver.get(LOGIN_URL)
        driver.implicitly_wait(TIMEOUT)

        logger.info("Login page opened successfully ")

        return driver

    except Exception as e:
        logger.error(f"Login Failed : {e}")
        print("Login Failed. Bot Stopped ")
        return None
