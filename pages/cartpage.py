from selenium.webdriver.common.by import By
from pages.Basepage import BasePage

class cartpage(BasePage):
    cart_item_name=(By.CSS_SELECTOR,"div.inventory_item_name")
    checkout_button_id=(By.ID,"checkout")

    def __init__(self,driver):
        super().__init__(driver)

    def get_cart_item_name(self):
        return self.get_element_text(self.cart_item_name)

    def click_checkout_button(self):
        self.click_element(self.checkout_button_id)
