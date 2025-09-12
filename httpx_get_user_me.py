import httpx

login_data = {
    "email": "test@example.com",
    "password": "12345"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_data)
login_response_data = login_response.json()
print("login_response:", login_response_data)
print("login Status code:", login_response.status_code)


headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
get_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print("Get_response:", get_response.json())
print("Get Status code:", get_response.status_code)