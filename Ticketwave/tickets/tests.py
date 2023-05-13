from django.test import TestCase
from .models import Ticket
from .serlializers import TicketSerializer

# Create your tests here.


class TicketTestCase(TestCase):
    def setUp(self):
        AmirSetup = Ticket.objects.create(
            name="Amir", State="Testing", price=12, Capacity=10
        )
        YoussefSetup = Ticket.objects.create(
            name="youssef", State="Testing", price=12, Capacity=1000
        )
        self.AmirSerializer = TicketSerializer(instance=AmirSetup)
        self.YoussefSerializer = TicketSerializer(instance=YoussefSetup)
        # record created in database

    def test_Ticket_Model(self):
        Amir = Ticket.objects.get(name="Amir")
        youssef = Ticket.objects.get(name="youssef")
        self.assertEqual(Amir.State, "Testing")
        self.assertEqual(youssef.State, "Testing")
        # test database record is created successfully

    def test_Ticket_Serializer(self):
        AmirData = self.AmirSerializer.data
        YoussefData = self.YoussefSerializer.data
        self.assertEqual(AmirData["name"], "Amir")
        self.assertEqual(YoussefData["name"], "youssef")
