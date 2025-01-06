import requests

# Here am defining  the base URL of the API
BASE_URL = "https://reqres.in/api/login"  # Am using a mock API for testing

# Test data
VALID_CREDENTIALS = {"email": "eve.holt@reqres.in", "password": "cityslicka"}  # Valid credentials
INVALID_CREDENTIALS = {"email": "invalid_email@reqres.in", "password": "wrongpassword"}  # Invalid credentials

def test_login_valid_credentials():
    """Test login with valid credentials."""
    response = requests.post(BASE_URL, json=VALID_CREDENTIALS)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "token" in response.json(), "Token not found in response"
    print("Test for valid credentials passed!")

def test_login_invalid_credentials():
    """Test login with invalid credentials."""
    response = requests.post(BASE_URL, json=INVALID_CREDENTIALS)
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"  # Here the mock API returns 400 for invalid login
    assert "error" in response.json(), "Error message not found in response"
    print("Test for invalid credentials passed!")

if __name__ == "__main__":
    print("Running tests...")
    test_login_valid_credentials()
    test_login_invalid_credentials()
    print("All tests completed successfully!")
