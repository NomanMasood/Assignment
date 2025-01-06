import random
import string
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import common as c
from features.pages.elements import Basket, Login, Products, Checkout
prev_price=0
import time
card_num=""
scenarios('../task4.feature')

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@given('I navigate to the Juice Shop login page')
def navigate_to_application(driver):
    driver.get("https://juice-shop.herokuapp.com/#/login")
    driver.maximize_window()
    time.sleep(5)
    driver = c.welcome_popup_handling(driver)
    #time.sleep(5)
    print("Page loaded successfully!!!")

@when('I login with valid generated credentials')
def login_with_generated_credentials(driver):
    json_data = c.fetch_json_file(f"..\\Assignment\\features\\test_data\\data.json")
    email = json_data['email']
    password= json_data['password']
    driver.find_element(By.XPATH, Login.email_xpath).send_keys(email)
    driver.find_element(By.XPATH, Login.pwd_xpath).send_keys(password)
    time.sleep(2)
    driver.find_element(By.XPATH, Login.login_btn_xpath).click()
    time.sleep(2)

@then('I should be logged in successfully')
def verify_successful_login(driver):
    time.sleep(3)
    dashboard_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, Products.all_prods_lbl_xpath))
    )
    assert dashboard_element is not None, "Login was not successful."
    print("Logged in successfully.")

@when(parsers.cfparse("I add the '{product}' to the basket"))
def add_product_and_verify(driver, product):
    time.sleep(3)
    all_prods = driver.find_elements(By.XPATH, "//div[@class='item-name']")
    for i in range(0,len(all_prods)):
        nme = all_prods[i].text
        if product in nme:
            cart_btn = all_prods[i].find_elements(By.XPATH, Products.add_to_bkt_btn_xpath)[i]
            driver.execute_script("arguments[0].click();", cart_btn)
            break
    print ("Item added to basket successfully")

@then(parsers.cfparse("I should see the '{products}' added success message"))
def verify_basketadded_success_message(driver, products):
    time.sleep(3)
    act_msg = driver.find_element(By.XPATH, Products.cart_suc_msg_xpath)
    assert f'Placed {products} into basket.' == act_msg.text or f'Added another {products} to basket.' == act_msg.text, f"{products} not added to basket."

@then(parsers.parse('the cart number should be updated to "{expected_cart_number}"'))
def verify_cart_number(driver, expected_cart_number):
    basket = driver.find_element(By.XPATH, Basket.your_basket_mm_xpath)
    basket_count_ele = basket.find_element(By.XPATH, 'following-sibling::span[1]')
    basket_count = int(basket_count_ele.text)
    assert basket_count == int(expected_cart_number), f"Expected cart count is : {expected_cart_number}, and actual is: {basket_count}"
    print (f"Actual cart count {basket_count} matched with expected count {expected_cart_number}")

@when('I navigate to my basket and increase the quantity of a product')
def increase_product_quantity(driver):
    driver.find_element(By.XPATH, Basket.your_basket_mm_xpath).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Basket.add_qty_btn_xpath).click()
    cnt_ele = driver.find_elements(By.XPATH, Basket.qty_btns_xpath)
    for i in range(0,len(cnt_ele)):
        if cnt_ele[i].text == '2':
            print ("Increased product quantity")

@when('I delete the product from the basket')
def delete_product_from_basket(driver):
    global prev_price
    prev_price_txt = driver.find_element(By.XPATH, Basket.prev_prc_xpath).text
    prev_price = prev_price_txt.split(': ')[1].rstrip('¤')
    delete_button = driver.find_element(By.XPATH, Basket.del_btn_xpath)
    delete_button.click()

@then('the total price should be updated')
def assert_total_price_updated(driver):
    time.sleep(3)
    total_price_txt = driver.find_element(By.XPATH, Basket.total_prc_xpath).text
    total_price = total_price_txt.split(': ')[1].rstrip('¤')
    assert float(total_price) < float(prev_price), "Total price did not change."
    print (f"Previous price {prev_price} changed to {total_price}")

@when('I click on checkout and add address information')
def click_checkout_and_add_address(driver):
    driver.find_element(By.XPATH, Checkout.chk_out_btn_xpath).click()
    driver.find_element(By.XPATH, Checkout.addrs_exp_xpath).click()
    time.sleep(3)
    driver.find_element(By.XPATH, Checkout.countryf_inp_xpath).send_keys('United States of America') # country
    driver.find_element(By.XPATH, Checkout.namef_inp_xpath).send_keys('Test')  # name
    driver.find_element(By.XPATH, Checkout.mobf_inp_xpath).send_keys('9293232323')  # mobile number
    driver.find_element(By.XPATH, Checkout.zipcodef_inp_xpath).send_keys('11419')  # zipcode
    driver.find_element(By.XPATH, Checkout.address_inp_xpath).send_keys('United States of America')  # address
    driver.find_element(By.XPATH, Checkout.cityf_inp_xpath).send_keys('Queens')  # city
    driver.find_element(By.XPATH, Checkout.statef_inp_xpath).send_keys('New York')  # state
    driver.find_element(By.XPATH, Checkout.sub_btn_xpath).click()
    time.sleep(3)

@when('I select the address and proceed to checkout')
def select_address(driver):
    time.sleep(5)
    sel_addr_ele = driver.find_element(By.XPATH, Checkout.sel_add_rdbox_xpath)
    try:
        sel_addr_ele.click()
        time.sleep(2)
    except:
        driver.execute_script("arguments[0].click();", sel_addr_ele)
    driver.find_element(By.XPATH, Checkout.continue_btn_xpath).click()
    time.sleep(3)
@when('I choose the delivery speed and proceed to checkout')
def choose_delivery_speed(driver):
    deliv_speed = driver.find_elements(By.XPATH , Checkout.del_speed_rdboxs_xpath)
    try:
        deliv_speed[0].click()
        time.sleep(4)
    except:
        driver.execute_script("arguments[0].click();", deliv_speed[0])
    driver.find_element(By.XPATH, Checkout.continue_btn_xpath).click()
    time.sleep(3)

@then('I should not have money in wallet balance')
def validate_wallet_balance(driver):
    wallet_blnc_txt = driver.find_element(By.XPATH, Checkout.wallet_blnc_xpath).text
    wallet_blnc = int(float(wallet_blnc_txt))
    assert wallet_blnc <= 0, f"Amount: {wallet_blnc} is available as wallet balance"
    print ("Wallet balance verification done")

@when('I add the details of new card and proceed to checkout')
def add_details_new_card(driver):
    global card_num
    card_num, expiry_month, expiry_year = c.generate_random_card_details()
    driver.find_element(By.XPATH, Checkout.add_new_card_xpath).click()    #added_card_sel_rdbox_id
    time.sleep(3)
    dropdown_month = driver.find_element(By.XPATH, Checkout.card_exp_mnt_inp_xpath)
    select = Select(dropdown_month)
    select.select_by_value(str(expiry_month))
    dropdown_year = driver.find_elements(By.XPATH, Checkout.card_exp_yr_inp_xpath)[1]
    select = Select(dropdown_year)
    select.select_by_value(str(expiry_year))
    driver.find_element(By.XPATH, Checkout.card_num_inp_xpath).send_keys(card_num)
    card_name = driver.find_elements(By.XPATH, Checkout.card_name_inp_xpath)
    card_name[1].send_keys("TestName")

    driver.find_element(By.XPATH , Checkout.sub_btn_xpath).click()
    time.sleep(3)

@then('I should see the card saved message')
def validate_card_saved_message(driver):
    act_msg = driver.find_element(By.XPATH, Checkout.cart_suc_msg_xpath).text
    exp_msg = f"Your card ending with {card_num[-4:]} has been saved for your convenience."
    assert act_msg==exp_msg, f"Actual message: {act_msg} is not matched with Expected message: {exp_msg}"
