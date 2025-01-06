# Built-in/Generic Imports
import json
import logging
import random
from faker import Faker
from locust import task, constant
from locust.contrib.fasthttp import FastHttpUser
log = logging.getLogger("rest-api-performance-test")
fake = Faker()

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
    log.error(f"{name}, {user_name}, {email}, {password}, {phone_number}")
    return payload


class LocustClient(FastHttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = constant(0)

    def __init__(self, environment):
        """ Class constructor."""
        super().__init__(environment)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task
    def load_rest_api_based_service(self):
        """ This method contains all the APIs that needs to be load tested for a service."""
        headers = get_headers()

        try:
            end_point = "/client_registeration"
            # Build your query parameter for GET API requests
            api_payload = get_api_payload()

            with self.client.post(end_point,headers=headers, catch_response=True, data=api_payload) as resp_of_api:

                if resp_of_api.status_code == 200:
                    #resp_body_of_api = resp_of_api.json()
                    #assert 'User Registered' in resp_body_of_api['msg']
                    resp_of_api.success()

                    # Avoid too much logging in load test script as it may slow it
                    log.info("API call resulted in success.")

                else:
                    err = resp_of_api.failure(resp_of_api.text)
                    # Avoid too much logging in load test script as it may slow it
                    log.error(f"API call resulted in failed. {err}")

        except Exception as e:
            log.error(f"Exception occurred! details are {e}")
