import requests

BASE_URL = "https://reqres.in/api"

def login(email, password):
    url = f"{BASE_URL}/login"

    payload={
        "email" : email,
        "password": password
    }

    headers = {
        "Content-Type": "application/jason"
    }

    response = request.post(
        url,
        json = payload,
        headers = headers
    )
    return response
    