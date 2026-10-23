import re
from pathlib import Path
from datetime import datetime
import pytest

from Browser.BrowseFactory import BrowserFactory

SCREENSHOT_DIR = Path(__file__).resolve().parent / "Screenshots"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshot whenever a test phase fails
    if report.failed:
        driver = None

        try:
            driver = BrowserFactory.Get_Driver()

            if driver is None:
                print("Screenshot skipped: WebDriver is unavailable.")
                return

            SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

            test_name = re.sub(r"[^\w.-]", "_", item.nodeid)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")

            screenshot_path = (
                SCREENSHOT_DIR / f"{test_name}_{timestamp}.png"
            )

            if driver.save_screenshot(str(screenshot_path)):
                print(f"\nScreenshot saved: {screenshot_path}")
            else:
                print("\nScreenshot could not be saved.")

        except Exception as exc:
            print(f"\nScreenshot hook error: {exc}")