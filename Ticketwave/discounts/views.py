from .models import Discounts
from .serializers import DiscountsSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

class manageDiscounts(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiscountsSerializer
    queryset = Discounts.objects.all()

class createDiscount(generics.CreateAPIView):
    serializer_class = DiscountsSerializer
    queryset = Discounts.objects.all()

@api_view(('GET',))
def listDiscountsByEvent(request, event_id):
    discounts = Discounts.objects.filter(event_id=event_id)
    serializer = DiscountsSerializer(discounts, many = True)
    return Response(serializer.data)