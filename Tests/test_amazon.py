from pathlib import Path
import sys
import time

import pytest

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
from Pages.FilterSection import FilterSection
from Pages.ChangeLanguage import ChangeLanguage
from Pages.HeaderSectionBase import HeaderSectionBase

from Pages.Cart import Cart;

class TestAmazon:
   
    @pytest.fixture(autouse=True)
    def PerTest(self):
        self._headerbase = HeaderSectionBase();
        self._filterBase = FilterSection();
        self._languagebase = ChangeLanguage();
        self._headerbase.navigate(URL)
        yield  self._headerbase
        # Teardown
        BrowserFactory.close_driver()
        
    # def test_validate_homepage_menu_link_working(self):
    #   self._headerbase.Select_Link_HeaderSection("Amazon Pay");
    #   title = self._headerbase.GetPageTitle();
    #   print(title)
    #   assert "Amazon Pay" in title, f"Expected 'Amazon Pay' in page but got :{title}"
    
    # def test_user_Search(self):
    #     self._headerbase.Search_Product("Iphone 18");
    #     count = self._filterBase.GetProductDetails();
    #     assert len(count) >= 2, "Expected at least 2 products"
    
    # def test_apply_Filter_product(self):
    #     self._headerbase.Search_Product("iphone");
    #     self._filterBase.FilterProductBy_StorageCapacity("128 GB")
    #     self.result = self._filterBase.GetProductDetails();
    #     self.compareText = " 128 GB";
    #     self.resultSet = [ x for x in self.result if  self.compareText.lower() in x.lower()]
    #     assert len(self.resultSet) >= 2, "Expected at least filter should have more than 2 "
    
    # def test_user_language_setting(self):
    #     self.languageForSelection = "नमस्ते. साइन इन";
    #     self._headerbase.Click_languageButton();
    #     self._languagebase.Select_Language("हिन्दी")
    #     accountListtext =  self._headerbase.GetAccountListText();
    #     print(f"Expected text: {self.languageForSelection}")
    #     print(f"Actual text:   {accountListtext}")
    #     assert self.languageForSelection in accountListtext, (
    #     f"Expected Hindi text '{self.languageForSelection}' "
    #     f"but got '{accountListtext}'")

    # def  test_user_can_Add_To_Cart(self):
    #     self._headerbase.Search_Product("mobile");
    #     self._filterBase.Click_Element_Cart();
    #     cartvalue  = self._headerbase.Get_CartCount();
    #     assert int(cartvalue) > 0, "Cart is not empty";  
    
    def test_user_UpdateQuanity(self):
        self._headerbase.Search_Product("hp laptop");
        self._filterBase.Click_Element_Cart();
        self._headerbase.Click_CartBtn();
        cart  = Cart();
        cart.UpdateQuanity();
        updateQuanity =  self._headerbase.Get_CartCount();
        assert updateQuanity == 2, f"Expected value for quantity does not match"
    
    def  test_User_Can_DeleteCartItem(self):
          self._headerbase.Search_Product("hp laptop");
          self._filterBase.Click_Element_Cart();
          self._headerbase.Click_CartBtn();
          cart  = Cart();
          cart.DeleteProduct();
          updateQuanity =  self._headerbase.Get_CartCount();
          assert updateQuanity == 0, f"Expected cart was not empty"
              

         
        
        
