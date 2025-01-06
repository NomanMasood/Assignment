import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from features.pages.elements import LandingPage, Registration, Products, Login
import random
import string
import time
import common as c

email = ''
password = ''
sec_ques = ''
ans = ''
scenarios('../task3.feature')
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
def generate_random_user_info():
    username = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
    email = f"{username}@example.com"
    password = "Password123!"
    sec_que = random.choice(LandingPage.lst_sec_ques)
    answer = random.choices(string.ascii_uppercase, k=15)
    return email, password, sec_que,answer

@given('I navigate to the user registration page')
def navigate_to_registration_page(driver):
    driver.get("https://juice-shop.herokuapp.com/#/register")
    driver.maximize_window()
    driver = c.welcome_popup_handling(driver)
    usr_reg_lbl = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, Registration.usr_reg_lbl_xpath)))
    print ("User Registration page loaded successfully")

@when('I trigger validation messages by clicking on all fields')
def trigger_validation_messages(driver):
    actions = ActionChains(driver)
    driver.find_element(By.ID,Registration.email_id).click()
    driver.find_element(By.ID,Registration.password_id).click()
    driver.find_element(By.ID,Registration.rep_password_id).click()
    time.sleep(1)
    for i in range(0, 3):
        actions.send_keys(Keys.TAB).perform()
    sec_ques = driver.find_element(By.XPATH,Registration.sec_quest_drop_xpath)
    time.sleep(1)
    driver.find_element(By.ID,Registration.answer_id).click()
    actions.send_keys(Keys.TAB).perform()

@then('I should see the validation message for all required input fields')
def validate_frontend_validation_message_on_registration_page(driver):
    fail_count = 0
    val_error_eles = driver.find_elements(By.XPATH, Registration.val_err_xpath)
    for ele in val_error_eles:
        if ele.text in Registration.lst_msgs:
            print (f"Validation message ('{ele.text}') is visible")
        else:
            fail_count = fail_count + 1
    assert fail_count<1, "Front end validation messages appeared for all required fields"
    print ("Validation message verified")

@when('I fill in the registration form with self-generated information')
def fill_registration_form(driver):
    global email, password, sec_ques, ans
    email, password, sec_ques, ans = generate_random_user_info()
    #driver.execute_script("return arguments[0].scrollIntoView();", driver.find_element(By.CSS_SELECTOR, "input[formControlName='repeatPassword']"))
    driver.find_element(By.ID,Registration.email_id).send_keys(email)
    driver.find_element(By.ID,Registration.password_id).send_keys(password)
    driver.find_element(By.ID,Registration.rep_password_id).send_keys(password)
    driver.find_element(By.XPATH,Registration.sec_quest_drop_xpath).click()
    lst_items = driver.find_elements(By.XPATH, "//div[@id='mat-select-0-panel']//mat-option//span")
    for items in lst_items:
        if items.text == sec_ques:
            items.click()
            time.sleep(1)
            break
    answer = driver.find_element(By.ID,Registration.answer_id).send_keys(ans)
    print ("All Mandatory fields are filled")

@when('I toggle the available control to show password advice')
def show_password_advice(driver):
    pwd_advc_chk = driver.find_element(By.CSS_SELECTOR, Registration.pass_adv_css)
    if pwd_advc_chk.is_selected():
        print ("Password Advice is already checked")
    else:
        pwd_advc_tog = pwd_advc_chk.find_element(By.XPATH, Registration.pass_adv_tog_xpath)
        pwd_advc_tog.click()
        time.sleep(2)
    print ("Successfully toggled the password advise control")

@then('I should be able to see correct information in show password advice section')
def validate_password_advise_section(driver):
    fail_count = 0
    adv_sec_ele = WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located((By.XPATH, Registration.pass_adv_expd_sec_xpath)))
    print("Password Advice section is visible. Now checking the specified password instructions!!!")
    for info in adv_sec_ele:
        if info.text in Registration.err_info:
            print(f"Validated Error Description: {info.text}")
        else:
            fail_count += 1
    assert fail_count < 1, "Password instructions are not as expected"
    print("Show Password Advice section's verification is done")

@when('I hit the register button')
def register_to_application(driver):
    driver.find_element(By.XPATH, Registration.register_btn_xpath).click()
    print ("Register button clicked successfully")

@then('I should see a successful registration message')
def verify_successful_registration(driver):
    time.sleep(5)
    suc_msg_ele = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, Products.cart_suc_msg_xpath)))
    assert 'Registration completed successfully. You can now log in.' == suc_msg_ele.text, "Registration was not successful."
    print("Registration successful message displayed.")
    valid_creds = {"email": email , "password": password}
    c.generate_json_file(valid_creds, f"C:\\Users\\nomanm\\PycharmProjects\\pythonProject\\Assignment\\features\\test_data")

@then('I should navigate to login page')
def validate_nav_to_login_page(driver):
    current_url = driver.current_url
    print("The current URL is:", current_url)
    assert current_url=='https://juice-shop.herokuapp.com/#/login'
    print ('User is successfully navigated to login page after successful user registration')

@when('I log in using the same information')
def login_to_application(driver):
    time.sleep(2)
    driver.find_element(By.XPATH, Login.email_xpath).send_keys(email)
    driver.find_element(By.XPATH, Login.pwd_xpath).send_keys(password)
    driver.find_element(By.XPATH, Login.login_btn_xpath).click()
    time.sleep(2)

@then('I should be logged in successfully')
def verify_successful_login(driver):
    dashboard_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, Products.all_prods_lbl_xpath))
    )
    assert dashboard_element is not None, "Login was not successful."
    print("Logged in successfully.")
