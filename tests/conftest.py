import os
from datetime import datetime
import pytest
from selenium import webdriver
from utilities import ReadConfigurations

@pytest.fixture()
def setup_and_teardown(request):
    browser=ReadConfigurations.read_configuration("basic info","browser")
    app_url=ReadConfigurations.read_configuration("basic info","url")

    if browser.lower()=="chrome":
        options= webdriver.ChromeOptions()
        # Disable Chrome's password breach popup on SauceDemo
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        driver=webdriver.Chrome(options=options)
    elif browser.lower()=="edge":
        driver=webdriver.Edge()
    else:
        print("Provide a valid browser name from the list")

    driver.maximize_window()
    driver.get(app_url)
    request.cls.driver=driver

    yield
    driver.quit()
