from pathlib import Path
import sys
import time

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
from Pages.FilterSection import FilterSection
from Pages.ChangeLanguage import ChangeLanguage
from Pages.Cart import Cart;

class HeaderSectionBase(AutomationBase):
    
 _driver:webdriver;
   
   
   
 def Select_Link_HeaderSection(self,linkName: str):
     try:
        headerLinks = self.find_UIElements(By.XPATH,"//div[@id='nav-xshop']//li")
        if headerLinks is None:
         raise
        for link in headerLinks:
            if link.text == linkName:
                try:
                    link.click();
                    return True
                except:
                    print("Error occured while clicking link");  
                    return False; 
     except Exception as e:
         print(f"Error occurred as {str(e)}");
         False

 def Search_Product(self,productName: str):
  try:
      if productName is None:
          raise "Preoduct name should not be null or Empty"
      searchTxt = self.find_UIElement(By.ID,"twotabsearchtextbox");
      searchTxt.send_keys(productName);
      time.sleep(2);
      btnEnter =  self.find_UIElement(By.ID,"nav-search-submit-button");
      btnEnter.click();
      time.sleep(2);
      print(f"Product Search Sucessfully  {productName}")
  except Exception as e:
      print(f"Error occured while searching product {str(e)}")                
        
 def Get_CartCount(self):
     try:
         print("fetching cart details");
         cartCount=  self.find_UIElement(By.ID,"nav-cart-count");
         print(f"Item in Cart Are {cartCount}")
         time.sleep(1);
         return int(cartCount.text);
     except Exception as e:
        print("Error occured while fetching Cart count");
        return -1; 
 def Click_CartBtn(self):
     try:
         print("clicking Cart Button");
         btn = self.find_UIElement(By.ID,"nav-cart-count");
         btn.click();
         time.sleep(1);
         print("Add to cart button clicked")
     except Exception  as e:
       print(f"Error occured while clicking Cart Button {str(e)}");
         
 def Click_languageButton(self):
      btnLan =  self.find_UIElement(By.ID,"icp-nav-flyout");
      btnLan.click();
      time.sleep(1);

    
 def GetAccountListText(self):
      return self.find_UIElement(By.ID,"nav-link-accountList").text;
  
 def GetPageTitle(self):
       return self._driver.title
   
  
# record = HeaderSectionBase()
# changeLan = ChangeLanguage();
# # filter = FilterSection();
# record.navigate(URL)
# record.Click_languageButton();

# changeLan.Select_Language("हिन्दी");
# data = record.GetAccountListText()

# text = "नमस्ते. साइन इन";
# checkmatch =  text in data;
# print(checkmatch);

# record.Search_Product("Iphone 18")
# filter.FilterProductBy_StorageCapacity("128 GB")
# result  = filter.GetProductDetails();

# compareText = " 128 GB";

# resultSet = [
#     x for x in result
#     if compareText.lower() in x.lower()
# ]
# print("result:", result)
# print("type:", type(result))

# filter.Click_Element_Cart();
# record.Click_CartBtn();
# cart  = Cart();

# cart.UpdateQuanity();
# itemsIncart =  record.Get_CartCount();