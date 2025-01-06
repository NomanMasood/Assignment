import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import common as c
from features.pages import elements as ele
from features.pages.elements import LandingPage
import time

prod_popup_ele = None
prod_name= None
welcome_popup = ele.WelcomePopup()
# Load feature scenarios from the feature file
scenarios('../task2.feature')

@pytest.fixture(scope="module")
def driver():
    # Setup WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Teardown WebDriver
    driver.quit()

@given('I navigate to the Juice Shop application')
def navigate_to_application(driver):
    driver.get("https://juice-shop.herokuapp.com/#/")
    driver.maximize_window()
    time.sleep(5)
    driver = c.welcome_popup_handling(driver)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("Page loaded successfully!!!")

@when("I click on the first product")
def click_on_product(driver):
    global prod_name
    product = driver.find_elements(By.XPATH, LandingPage.all_prods_xpath)[0]
    prod_name = product.get_attribute("alt")
    product.click()
    time.sleep(5)
    print ("Clicked on Product")


@then('I should see the product pop-up')
def verify_product_popup(driver):
    global prod_popup_ele
    prod_popup_ele = driver.find_element(By.XPATH, LandingPage.prod_popup_xpath)
    assert prod_popup_ele is not None, "Product pop-up did not appear."
    print("Product pop-up appeared.")

@then('the product image should be displayed')
def verify_product_image(driver):
    print (prod_name, prod_popup_ele)
    product_image = prod_popup_ele.find_element(By.XPATH, f"//img[@alt='{prod_name}']")
    assert product_image.is_displayed(), "Product image is not displayed."
    print("Product image is displayed.")

@when('I expand the review section if available')
def expand_review_section(driver):
    try:
        review_section = prod_popup_ele.find_element(By.XPATH, LandingPage.rev_sec_xpath)
        review_section.click()
    except Exception:
        print("No reviews section available to expand.")

@then('I should be able to see the expanded review section')
def check_expanded_review_section(driver):
    time.sleep(2)
    exp_rev_ele = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, LandingPage.exp_rev_sec_xpath)))
    exp_rev = exp_rev_ele.get_attribute("style")
    assert "visibility: visible" in exp_rev, "Review section is not expanded."
    print ("Expanded review section verified")

@then('I close the product pop-up')
def close_product_form(driver):
    try:
        close_button = prod_popup_ele.find_element(By.XPATH, LandingPage.prod_pop_close_btn_xpath)
        close_button.click()
    except:
        print ("Unable to find/click the close button")
    print("Closed the product form.")
