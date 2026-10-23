from pathlib import Path
import sys
import time;
project_root = str(Path(__file__).resolve().parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
from Browser.BrowseFactory import BrowserFactory;
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from settings import BROWSER_NAME, EXPLICIT_TIMEOUT
from abc import ABC
from typing import List, Optional


class AutomationBase(ABC):
    
 _driver:webdriver;
 _wait:WebDriverWait
 
 def __init__(self):
     self._driver = None
     self._driver = self.Initialize_Driver();
     self._wait = WebDriverWait(self._driver, EXPLICIT_TIMEOUT)
 
 def Initialize_Driver(self):
     if self._driver is None:
         self._driver = BrowserFactory.Create_Driver(BROWSER_NAME)
     return self._driver
    
 def find_UIElement(self, by: By, locator: str) -> Optional[WebElement]:
        print(f"finding element By {by} and Locator name is {locator}")
        try:
            return self._wait.until(
                EC.presence_of_element_located((by, locator))
            )
        except Exception as e:
            print(f"Error occured while finding  element by {by} with locator {locator}: {e}")
            return None
        
 def find_UIElements(self, by: By, locator: str) -> List[WebElement]:
        print(f"finding elements By {by} and Locator name is {locator}")
        try:
            return self._wait.until(
                EC.presence_of_all_elements_located((by, locator))
            )
        except Exception as e:
            print(f"Error occured while finding elements by {by} with locator {locator}: {e}")
            return []

 def enter_text(self, by: By, locator: str, text: str) -> bool:
        print(f"Entering text into element By {by} with locator {locator}")
        element = self.find_UIElement(by, locator)
        if element is None:
            return False

        try:
            element.clear();
            element.send_keys(text)
            print(f" Following Text is Entered  {text}");
            return True
        except WebDriverException as e:
            print(f"Error occurred while entering text by {by} with locator {locator}: {e}")
            return False

 def navigate(self, url: str) -> None:
      if url is None:
          raise ValueError("URL is null || Empty")
      self._driver.get(url)
      time.sleep(5)
    
def GetPageTitle(self):
    return self._driver.title

def CloseBrowser():
     BrowserFactory.close_driver();

         
       
    
    
            
       
        