from django.test import TestCase
from .models import TicketClass
import json
import requests



# Create your tests here.

class TicketClassTestCase(TestCase):
    def setUp(self):
        TicketClass.objects.create(name="Amir", category="Testing", subcategory="subtest", amount=10)
        TicketClass.objects.create(name="youssef", category="Testing", subcategory="subtest", amount=1000)
        #record created in database
        
    def Test_TicketClass_Model(self):
        Amir= TicketClass.objects.get(name="Amir")
        youssef= TicketClass.objects.get(name="youssef")
        self.assertEqual(Amir.name, "Amir")
        self.assertEqual(youssef.name, "youssef")
        # test database record is created successfully
    
    def TestTicketClassEndpointCreate(self):  #testing create
        url="127.0.0.1:8000/ticket_classes/create"
        data= json.dumps({
            "name":"Abdallah", 
            "category": "endpoint testing",
            "subcategory": "subcategory is testing",
            "amount": 100
        })
        headers= {
            'Content-Type':'application/json'    #specify content type as json object
        }
        response= requests.post(url=url,data=data,headers=headers)
        self.assertEqual(response.status_code, 201)


    def TestTicketClassEndpointGetAll(self):  #testing get all
        url="127.0.0.1:8000/ticket_classes/get"
        response= requests.get(url=url)
        self.assertEqual(response.status_code, 200) 

    def TestTicketClassEndpointUpdate(self):  #testing update
        url="127.0.0.1:8000/ticket_classes/update/2"
        data= json.dumps({
            "amount":"500", 
        })
        headers= {
            'Content-Type':'application/json'    #specify content type as json object
        }
        response= requests.put(url=url,data=data,headers=headers)
        self.assertEqual(response.status_code, 200) 