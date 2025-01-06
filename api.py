import requests
from faker import Faker
fake = Faker()

url = 'http://127.0.0.1:5000/client_registeration'

# Define the payload with form-encoded data
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

# Set the headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Send the POST request
response = requests.post(url, headers=headers, data=payload)
if response.status_code == 200:
    resp_body_of_api = response.json()
    assert 'User Registered' in resp_body_of_api['msg']
    print('Status Code:', response.status_code)
    print('Response Body:', response.json())
