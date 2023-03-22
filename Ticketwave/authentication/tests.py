import unittest
from rest_framework.request import Request
import requests
import json


class Tests(unittest.TestCase):

    def test_register(self):

        url = "http://localhost:8000/auth/signup/"
        payload = json.dumps({
            "username": "ziadamr",
            "email": "ziadamr@gmail.com",
            "password1": "poiuytpoiuyt",
            "password2": "poiuytpoiuyt",
            "is_public": True,
            "image_id": 1
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200, "incorrect status code")

    def test_send_verification_email(self):
        url = "http://localhost:8000/auth/send_verification_email/1/"
        payload = json.dumps({})
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200, "incorrect status code")

    def test_send_password_reset(self):
        url = "http://localhost:8000/auth/password/reset/ziadamr/ziadamr@gmail.com/"
        payload = json.dumps({})
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200, "incorrect status code")
    
    def test_login(self):
        url = "http://localhost:8000/auth/login/"
        payload = json.dumps({
            "username": "ziadamr",
            "email": "ziadamr@gmail.com",
            "password": "poiuytpoiuyt",
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        
        print(response.status_code)
        self.assertEqual(response.status_code, 400, "you haven't opened the verification email yet")
        #self.assertEqual(response.status_code, 201, "incorrect status code")

unittest.main()
