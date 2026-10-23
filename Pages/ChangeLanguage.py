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
from settings import BROWSER_NAME, EXPLICIT_TIMEOUT,URL
from Pages.AutomationBase import AutomationBase

class ChangeLanguage(AutomationBase):
    
 _saveChanges:WebElement = None
  
    
 def Select_Language(self,language: str):
    try:
        if language is None:
            raise ValueError("Language is null");
        else:
            userLanguage = self.find_UIElements(By.XPATH,"//div[@id='icp-language-settings']//input");
     
            print(f"Selecting user language: {language}")
            for x in userLanguage:
                if  language.upper() in x.accessible_name.upper():
                    # radio = x.find_element(By.CLASS_NAME,'a-icon a-icon-radio')
                    # radio.click();
                    self._driver.execute_script("arguments[0].click();", x)
                    print("user language selected");
                    time.sleep(2);
                    break
            btnSave = self.find_UIElement(By.XPATH,"//input[@class='a-button-input']");
            btnSave.click();   
            time.sleep(2); 
    except Exception as ex:
       print(f"Error occured while selecting language {str(ex)}") 
    
