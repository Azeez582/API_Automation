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
"""
here whai got is we are sending a post request where response = request.post (url,json=payloads,headers=headers)
here we have defined the url = Base_url/login paylods are defined as {email,password} json format headers  defined as content-type :application/json so 
these variables will get utilised in fetching the response and we are validatinfg by saying that token shoud be preent in
data where data = context.response.json()"""