from selenium.webdriver.common.by import By
from pages.Basepage import BasePage

class checkoutpage(BasePage):
    first_name_id=(By.ID,"first-name")
    last_name_id=(By.ID,"last-name")
    postal_code_id=(By.ID,"postal-code")
    continue_button_id=(By.ID,"continue")
    finish_button_id=(By.ID,"finish")
    complete_header=(By.CSS_SELECTOR,"h2.complete-header")

    def __init__(self,driver):
        super().__init__(driver)

    def enter_checkout_information(self,first_name,last_name,postal_code):
        self.type_text(self.first_name_id,first_name)
        self.type_text(self.last_name_id,last_name)
        self.type_text(self.postal_code_id,postal_code)

    def click_continue(self):
        self.click_element(self.continue_button_id)

    def click_finish(self):
        self.click_element(self.finish_button_id)

    def get_order_confirmation_message(self):
        return self.get_element_text(self.complete_header)
    
