from selenium.webdriver.common.by import By
from pages.Basepage import BasePage

class inventorypage(BasePage):
    page_title=(By.CSS_SELECTOR,"span.title")
    add_backpack_button_id=(By.ID,"add-to-cart-sauce-labs-backpack")
    cart_badge=(By.CSS_SELECTOR,"span.shopping_cart_badge")
    cart_link= (By.CSS_SELECTOR, "a.shopping_cart_link")

    def __init__(self,driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.get_element_text(self.page_title)

    def add_backpack_to_cart(self):
        self.click_element(self.add_backpack_button_id)

    def get_cart_badge_count(self):
        return self.get_element_text(self.cart_badge)

    def click_shopping_cart(self):
        self.click_element(self.cart_link)
