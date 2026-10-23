from pathlib import Path
import sys
from threading import local

project_root = str(Path(__file__).resolve().parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from Browser.EdgeBrowser import EdgeBrowser
from Browser.ChromeBrowser import ChromeBrowser
from settings import BROWSER_NAME


class BrowserFactory:
    _thread_state = local()

    @staticmethod
    def Create_Driver(browserName: str = BROWSER_NAME):
        drivers = getattr(BrowserFactory._thread_state, "drivers", None)
        if drivers is None:
            drivers = {}
            BrowserFactory._thread_state.drivers = drivers

        browser_name = browserName.upper()
        if browser_name not in drivers:
            match browser_name:
                case "CHROME":
                    driver = ChromeBrowser().launch_Chrome_Browser()
                case "EDGE":
                    driver = EdgeBrowser().launch_edge_browser()
                case _:
                    raise ValueError(f"Unsupported browser: {browserName}")
            drivers[browser_name] = driver
        return drivers[browser_name]

    @staticmethod
    def close_driver(browserName: str = BROWSER_NAME):
        drivers = getattr(BrowserFactory._thread_state, "drivers", {})
        browser_name = browserName.upper()
        driver = drivers.pop(browser_name, None)
        if driver is not None:
            driver.quit()


factory = BrowserFactory.Create_Driver();
