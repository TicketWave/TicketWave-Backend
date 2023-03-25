from django.test import TestCase
from .models import Event,Event_private
# Create your tests here.
class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(name="Amir", summary="Testing", description="subtest", url="https://www.google.com.eg/?hl=ar",start="10-02-2000",end="15-03-2004",status="busy",online_event=True,hide_start_date=False,hide_end_date=False)
        Event_private.objects.create (listed=True,shareable=False,invite_only= False,show_remaining= True,password="Amir",capacity=15,capacity_is_custom= True,event=1)      
        #record created in database
        
    def Test_Event_Model(self):
        Amir= Event.objects.get(name="Amir")
        Private=  Event_private.objects.get(event=1)
        self.assertEqual(Amir.name, "Amir")
        self.assertEqual(Private.listed, True)
        # test database record is created successfully
    

