from selenium.webdriver.common.by import By
from pages.Basepage import BasePage

class loginpage(BasePage):
    username_field_id=(By.ID,"user-name")
    password_field_id=(By.ID,"password")
    login_button_id=(By.ID,"login-button")
    error_message=(By.CSS_SELECTOR,"h3[data-test='error']")

    def __init__(self,driver):
        super().__init__(driver)

    def enter_username(self,username):
        self.type_text(self.username_field_id,username)

    def enter_password(self,password):
        self.type_text(self.password_field_id,password)

    def click_login_button(self):
        self.click_element(self.login_button_id)

    def login_to_application(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message_text(self):
        return self.get_element_text(self.error_message)
    