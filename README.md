# SauceDemo Automation Project

Automated UI tests for SauceDemo using Python, Selenium, and Pytest with Page Object Model (POM).

## Tech Stack
- Python
- Selenium WebDriver
- Pytest
- pytest-html

## Project Structure
- config/ - stores base URL and browser settings in config.ini
- pages/ - page object classes (Basepage, loginpage, inventorypage, cartpage, checkoutpage)
- tests/ - pytest fixtures and test cases (test_login, test_checkout)
- utilities/ - helper module to read config.ini

## Test Cases Covered
- Valid user login verification
- Negative login scenarios using pytest parametrize (invalid credentials, locked-out user, empty username)
- End-to-end checkout flow (add to cart, verify cart, fill checkout details, verify order confirmation)

## How to Run

1. Clone the repo
git clone https://github.com
cd saucedemo-selenium-pytest

2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run tests with HTML report
pytest -v --html=report.html
