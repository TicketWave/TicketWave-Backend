from django.test import TestCase
from .models import Ticket
import json
import requests



# Create your tests here.


class TicketTestCase(TestCase):
    def setUp(self):
        AmirSetup=Ticket.objects.create(name="Amir", category="Testing", subcategory="subtest", amount=10)
        YoussefSetup=Ticket.objects.create(name="youssef", category="Testing", subcategory="subtest", amount=1000)
        self.AmirSerializer=TicketSerializer(AmirSetup)
        self.YoussefSerializer=TicketSerializer(YoussefSetup)
    
        #record created in database
        
    def Test_Ticket_Model(self):
        Amir= Ticket.objects.get(name="Amir")
        youssef= Ticket.objects.get(name="youssef")
        self.assertEqual(Amir.category, "Testing")
        self.assertEqual(youssef.category, "Testing")
        # test database record is created successfully
    
    def TestTicketSerializer(self):
        AmirData=self.AmirSerializer.data
        YoussefData=self.YoussefSerializer.data
        self.assertEqual(AmirData["name"], "Amir")
        self.assertEqual(YoussefData["name"], "youssef")