import unittest
from rest_framework.request import Request
import requests
import json


class Tests(unittest.TestCase):

    def runTest_register(self):

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

    def runTest_login(self):
        url = "http://localhost:8000/auth/login/"
        payload = json.dumps({
            "email": "ziadamr@gmail.com",
            "password": "poiuytpoiuyt",
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        
        self.assertEqual(response.status_code, 200, "incorrect status code")

    def runTest_send_verification_email(self):
        url = "http://localhost:8000/auth/send_verification_email/1/"
        payload = json.dumps({})
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200, "incorrect status code")

    def runTest_send_password_reset(self):
        url = "http://localhost:8000/auth/password/reset/ziadamr/ziadamr@gmail.com/"
        payload = json.dumps({})
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200, "incorrect status code")


unittest.main()
