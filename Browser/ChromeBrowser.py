from pathlib import Path
import sys

project_root = str(Path(__file__).resolve().parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from settings import (HEADLESS_MODE,IMPLICIT_TIMEOUT)

class ChromeBrowser:
    _driver: webdriver.Chrome | None

    def __init__(self):
        self._driver = None
        self._chromeOptions = ChromeOptions()
        self._chromeOptions.add_argument("--start-maximized")
        if HEADLESS_MODE:
            self._chromeOptions.add_argument("--headless=new")
            self._chromeOptions.add_argument("--disable-gpu")
            print("Headless mode enabled.");

    def launch_Chrome_Browser(self):
        print("Launching Chrome browser")
        if self._driver is None:
            try:
                self._driver = webdriver.Chrome(options=self._chromeOptions)
                self._driver.implicitly_wait(IMPLICIT_TIMEOUT * 60)
            except Exception as e:
                print(f"Error occurred while launching Chrome browser: {e}")
                raise
        return self._driver
