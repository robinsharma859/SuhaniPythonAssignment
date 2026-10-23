
from pathlib import Path
import sys

project_root = str(Path(__file__).resolve().parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from settings import HEADLESS_MODE, IMPLICIT_TIMEOUT


class EdgeBrowser:
    _driver: webdriver.Edge | None
    _options: EdgeOptions

    def __init__(self):
        self._driver = None
        self._options = EdgeOptions()
        self._options.add_argument("--start-maximized")

        if HEADLESS_MODE:
            self._options.add_argument("--headless=new")
            self._options.add_argument("--disable-gpu")
            print("Headless mode enabled.")

    def launch_edge_browser(self):
        try:
            print("Launching Edge browser")
            self._driver = webdriver.Edge(options=self._options)
            self._driver.implicitly_wait(IMPLICIT_TIMEOUT * 60)
            print("Edge browser launched successfully.")
            return self._driver

        except Exception as e:
            print(f"Error occurred while launching Edge browser: {e}")
            raise
