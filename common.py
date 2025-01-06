from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages import elements
import allure
import json
import time
import random
from datetime import datetime
import os
import functools


def get_project_path():
    current_path = ""
    str_currentdir_path = current_path
    str_currentdir_name = os.path.basename(str_currentdir_path)
    while not str_currentdir_name == "features":
        if os.sep + "features" in str_currentdir_path:
            str_currentdir_path = os.path.dirname(os.path.abspath(str_currentdir_path))
            str_currentdir_name = os.path.basename(str_currentdir_path)

        else:
            str_currentdir_path = os.path.abspath(str_currentdir_path) + os.sep + "features"
            str_currentdir_name = os.path.basename(str_currentdir_path)
    return os.path.dirname(str_currentdir_path)

def generate_random_card_details():
    card_number = ''.join([str(random.randint(0, 3)) for _ in range(16)])
    expiry_month = random.randint(1, 12)
    current_year = datetime.now().year
    expiry_year = random.randint(2080, 2100)
    return card_number, expiry_month, expiry_year

def welcome_popup_handling(driver):
    try:
        welcome_popup = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                       "app-welcome-banner[class='ng-star-inserted'] div[class='mat-typography']")))
        if welcome_popup is not None:
            print("Welcome Popup appeared")
            dismis_popup = driver.find_element(By.XPATH, "//span[normalize-space()='Dismiss']")
            dismis_popup.click()
            print("Dismissed the Welcome pop up")
        else:
            print("No Welcome Popup appeared")
        return driver
    except Exception as ex:
        print ("Unexpected error appeared while handling the welcome popup: " + str(ex))

def generate_json_file (data, file_path):

    with open(file_path+'\data.json', 'w') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))

def fetch_json_file(file_path):
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def parse_data_table(pstr_text, pstr_orient='dict'):
    try:
        parsed_text = [
            [x.strip() for x in line.split('|')]
            for line in [x.strip().strip('|') for x in pstr_text.splitlines()]
        ]
        header, *data = parsed_text
        if pstr_orient == 'dict':
            return [
                dict(zip(header, line))
                for line in data
            ]
        else:
            if pstr_orient == 'columns':
                data = [
                    [line[i] for line in data]
                    for i in range(len(header))
                ]
            return header, data
    except Exception as e:
        print(str(e))

def data_table(pstr_name, pstr_fixture='data', pstr_orient='dict'):
    try:
        formatted_str = '{name}\n{{{fixture}:DataTable}}'.format(
            name=pstr_name,
            fixture=pstr_fixture,
        )
        data_table_parser = functools.partial(parse_data_table, pstr_orient=pstr_orient)
        return parsers.cfparse(formatted_str, extra_types=dict(DataTable=data_table_parser))
    except Exception as e:
        print(str(e))
