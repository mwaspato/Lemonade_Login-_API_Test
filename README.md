Login API Test
This script tests the login functionality of an API by making POST requests with valid and invalid credentials. For demonstration purposes, it uses the reqres.in mock API, which simulates a login process.

Prerequisites
Python 3.x
requests library installed (install it using pip install requests)
Overview
The script performs the following tests:

Valid Credentials Test: Sends a POST request to the login endpoint with valid credentials and expects a status code of 200 and a token in the response.
Invalid Credentials Test: Sends a POST request to the login endpoint with invalid credentials and expects a status code of 400 and an error message in the response.
Setup
Clone the repository or download the script.

Install the required libraries:
pip install requests
The script is located in the file login_api_test.py.

How It Works
The script sends POST requests to the mock login endpoint at https://reqres.in/api/login with two sets of test credentials: one valid and one invalid. The valid credentials will return a 200 status code and a token, while the invalid credentials will return a 400 status code and an error message.

Running the Test
To run the script, simply execute it using Python:

bash
Copy code
python login_api_test.py
The expected output should be:
Running tests...
Test for valid credentials passed!
Test for invalid credentials passed!
All tests completed successfully!
Key Changes in the Script
Replaced the original API URL with the valid endpoint from reqres.in.
Updated the test data to include both valid and invalid credentials.
Adjusted the status code expectation for invalid credentials (the mock API returns a 400 status code instead of 401).
This description provides clear instructions for setting up, understanding, and running the test script, along with key changes made for testing purposes.
