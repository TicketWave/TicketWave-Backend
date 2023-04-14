from django.test import TestCase
from .models import Ticket
import json
import requests



# Create your tests here.

class TicketTestCase(TestCase):
    def setUp(self):
        Ticket.objects.create(name="Amir", category="Testing", subcategory="subtest", amount=10)
        Ticket.objects.create(name="youssef", category="Testing", subcategory="subtest", amount=1000)
        #record created in database
        
    def Test_Ticket_Model(self):
        Amir= Ticket.objects.get(name="Amir")
        youssef= Ticket.objects.get(name="youssef")
        self.assertEqual(Amir.name, "Amir")
        self.assertEqual(youssef.name, "youssef")
        # test database record is created successfully
    
    def TestTicketEndpointCreate(self):  #testing create
        url="127.0.0.1:8000/tickets/create"
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


    def TestTicketEndpointGetAll(self):  #testing get all
        url="127.0.0.1:8000/tickets/get"
        response= requests.get(url=url)
        self.assertEqual(response.status_code, 200) 

    def TestTicketEndpointUpdate(self):  #testing update
        url="127.0.0.1:8000/tickets/update/2"
        data= json.dumps({
            "amount":"500", 
        })
        headers= {
            'Content-Type':'application/json'    #specify content type as json object
        }
        response= requests.put(url=url,data=data,headers=headers)
        self.assertEqual(response.status_code, 200) 
