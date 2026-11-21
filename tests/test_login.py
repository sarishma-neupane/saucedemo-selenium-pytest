import pytest
from pages.loginpage import loginpage
from pages.inventorypage import inventorypage

@pytest.mark.usefixtures("setup_and_teardown")
class Testlogin:
    def test_valid_login(self):
        login_page=loginpage(self.driver)
        login_page.login_to_application("standard_user","secret_sauce")

        inventory_page=inventorypage(self.driver)
        assert inventory_page.get_page_title()=="Products"

    @pytest.mark.parametrize("username, password, expected_error", [
        ("wrong_user", "wrong_pass", "Username and password do not match any user in this service"),
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
        ("", "secret_sauce", "Username is required"),
    ])
    def test_invalid_login(self,username,password,expected_error):
        login_page=loginpage(self.driver)
        login_page.login_to_application(username,password)
        assert expected_error in login_page.get_error_message_text()