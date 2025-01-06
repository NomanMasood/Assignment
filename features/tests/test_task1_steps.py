import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import common as c
from features.pages.elements import LandingPage

lst=[]

scenarios('../task1.feature')

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


@when('I scroll to the bottom of the page')
def scroll_to_bottom(driver):
    print (driver.execute_script("document.documentElement.scrollHeight;"))
    #time.sleep(10)
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)
    print(str(driver.execute_script("document.documentElement.scrollHeight;")))
    print ("page scroll down completed")

@when('I change items per page to the maximum')
def change_items_per_page(driver):
    itemas_combox = driver.find_element(By.XPATH , LandingPage.items_cmbx_xpath)
    itemas_combox.click()
    lstbox = driver.find_elements(By.XPATH, LandingPage.items_cmbx_lstbx_xpath)
    for ele in lstbox:
        lst.append(ele.text)
    print("Available options:", lst)
    lstbox[-1].click()
    time.sleep(2)
    is_loaded = driver.execute_script("return document.readyState") == "complete"
    if is_loaded:
        print ("Page loaded successfully")
    else:
        print("page not loaded successfully")

@then('I should see all items displayed on the products page')
def verify_items_displayed(driver):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(5)
    actual_items = driver.find_elements(By.XPATH, LandingPage.prod_grids_xpath)
    exp_items = str(driver.find_element(By.XPATH , LandingPage.prod_disply_range_label_xpath).text).split()
    assert len(actual_items) == int(exp_items[-1]), "No items are displayed on the products page."
    print(f"Total items displayed: {exp_items[-1]}")
