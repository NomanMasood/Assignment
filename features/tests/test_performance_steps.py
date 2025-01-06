import logging
import pytest
import os
from faker import Faker
from pytest_bdd import scenarios, given, when, then, parsers
from locust import HttpUser, task, between, events, constant
import requests

log = logging.getLogger("rest-api-performance-test")
fake = Faker()

scenarios('../performanceTest.feature')


def get_headers():
    """ It generated the api headers."""
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    return headers

def get_api_payload():
    """ It generated the body of request."""
    name = fake.name()
    user_name = fake.user_name()
    email = fake.email()
    password = fake.password()
    phone_number = fake.phone_number()
    payload = {
        'fullName': name,
        'userName': user_name,
        'email': email,
        'password': password,
        'phone': phone_number
    }
    return payload

class LocustClient(HttpUser): # FastHttpUser
    host = "http://127.0.0.1:5000"
    wait_time = constant(0)

    @task
    def load_rest_api_based_service(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        api_payload = {
            'fullName': 'Test User',
            'userName': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'phone': '1234567890'
        }
        with self.client.post("/client_registeration", headers=headers, data=api_payload) as resp_of_api:
            if resp_of_api.status_code == 200:
                log.info("API call resulted in success.")
            else:
                log.error(f"API call resulted in failed. {resp_of_api.text}")

@given(parsers.cfparse('the {endpoint} is running'))
def api_is_running(endpoint):
    url = "http://127.0.0.1:5000"+endpoint
    url = url.replace("'","")
    if endpoint=="/client_login":
        response = requests.post(url, headers=get_headers(), data=get_api_payload())
    else:
        response = requests.post(url, headers=get_headers(), data=get_api_payload())
    assert response.status_code == 200, f"API is not running: {url}"
#        resp_body_of_api = response.json()
#        assert 'User Registered' in resp_body_of_api['msg']
#        print('Status Code:', response.status_code)
#        print('Response Body:', response.json())
    log.info("API is running.")


@when(parsers.parse('I send {user_count:d} registration requests with a spawn rate of {spawn_rate:d} over {duration}'))
def send_registration_requests(user_count, spawn_rate, duration):
    """This step simulates sending registration requests."""
    # Set environment variables for Locust
    os.environ["USER_COUNT"] = str(user_count)
    os.environ["SPAWN_RATE"] = str(spawn_rate)

    # Log the parameters for clarity
    log.info(f"Starting load test with {user_count} users, spawn rate of {spawn_rate} users/sec over {duration}.")


@then('the response should be successful')
def response_should_be_successful():
    """This step can include assertions to check the success of the responses."""
    log.info("Expecting the response to be successful.")
