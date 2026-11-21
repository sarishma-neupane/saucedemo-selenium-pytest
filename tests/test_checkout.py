import pytest
from pages.loginpage import loginpage
from pages.inventorypage import inventorypage
from pages.cartpage import cartpage
from pages.checkoutpage import checkoutpage


@pytest.mark.usefixtures("setup_and_teardown")
class TestCheckout:

    def test_end_to_end_checkout(self):
        #1. Login
        login_page = loginpage(self.driver)
        login_page.login_to_application("standard_user", "secret_sauce")

        # 2. Add product to cart & verify badge count
        inventory_page = inventorypage(self.driver)
        inventory_page.add_backpack_to_cart()
        assert inventory_page.get_cart_badge_count() == "1"
        inventory_page.click_shopping_cart()

        # 3. Verify item in cart & click checkout
        cart_page = cartpage(self.driver)
        assert cart_page.get_cart_item_name() == "Sauce Labs Backpack"
        cart_page.click_checkout_button()

        # 4. Complete checkout info & finish order
        checkout_page = checkoutpage(self.driver)
        checkout_page.enter_checkout_information("Sarishma", "Neupane", "44600")
        checkout_page.click_continue()
        checkout_page.click_finish()

        # 5. Verify order confirmation
        assert checkout_page.get_order_confirmation_message() == "Thank you for your order!"
