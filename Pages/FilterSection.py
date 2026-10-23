from pathlib import Path
import sys
import time;
project_root = str(Path(__file__).resolve().parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from typing import List

from Browser.BrowseFactory import BrowserFactory;
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from settings import BROWSER_NAME, EXPLICIT_TIMEOUT,URL
from Pages.AutomationBase import AutomationBase


class FilterSection(AutomationBase):
    
 _driver:webdriver;
 

 def FilterProductBy_StorageCapacity(self,filterByValue: str) -> bool:
    try:
        if filterByValue is None:
         raise ValueError("The Filtery by clause is null")
        filterCheckBoxs =  self.find_UIElements(By.XPATH,"//ul[@id='filter-p_n_g-1003492455111']//li//a");
        countRecords =  len(filterCheckBoxs)
        if countRecords > 0:
            print("check boxes found for Filteration");
            for checkbox in filterCheckBoxs:
                if checkbox.text == filterByValue:
                  try:
                     checkbox.click();
                     time.sleep(2);
                     return True
                  except:
                     print("Error occured while clicking link");  
                     return False; 
        else:
            raise Exception("No checkboxes were found on the page matching the filter path.")
    except Exception as e:
        print(f"Error occured while FilterBy Storage Capacity {str(e)}")
        return False
   
 def GetProductDetails(self) -> List[str]:
       records : list[str] =[]
       try:
           productDetails = self.find_UIElements(By.XPATH,"//div[@role='listitem']/following-sibling::div//h2[@aria-label]");
           if len(productDetails) > 0:
               for row in productDetails:
                text  = row.text.strip();
                if text:
                    records.append(text)              
           else:
               raise ValueError("Product details list is empty")
           print(f"product Details : {records}")
           return records;
       except Exception as e:
           print(f"error occured while fetching product details");
           return records;
       
 def Click_Element_Cart (self):
    try:
        print("Clicking Add to Cart button")
        btnCart = self.find_UIElement(By.XPATH,"//input[@name='submit.addToCart']");
        btnCart.click();
        print("Add to Cart is clicked");
        time.sleep(3);
    except Exception as e:
        print(f"Error occured while Clicking Add to Cart {str(e)}");