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

class Cart(AutomationBase):
    
 _parentDiv:WebElement=None 
 def __init__(self):
       super().__init__()
       self._parentDiv = self.find_UIElement(By.CLASS_NAME,"a-stepper-controls")
  
 def UpdateQuanity(self,quantity=2):
    try:
        print("Updating quantity");
        update = self._parentDiv.find_element(By.XPATH,"//button[@data-a-selector='increment']");
        for _ in range(quantity-1):
            update.click();
            time.sleep(1);

            print("Value updated in cart");              
    except Exception as e:
     print(f"Error occured while upadating Quantity {str(e)}")  

 def GetCartQuanity(self):
     return self._parentDiv.find_element(By.XPATH,"//span[@data-a-selector='inner-value']").text;
 
 def DeleteProduct(self):
     try:
         print("Deleting product from Cart");
         deleteButton =  self.find_UIElement(By.XPATH,"//input[@data-feature-id='item-delete-button']")
         deleteButton.click();
         time.sleep(2);

     except Exception as e:
         print(f"Error occured while deleting product {str(e)}")