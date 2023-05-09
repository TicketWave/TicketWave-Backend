from .models import Discounts
from .serializers import DiscountsSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime


class manageDiscounts(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiscountsSerializer
    queryset = Discounts.objects.all()
    lookup_field = "id"


class createDiscount(generics.CreateAPIView):
    serializer_class = DiscountsSerializer
    queryset = Discounts.objects.all()


@api_view(("GET",))
def listDiscountsByEvent(request, event_id):
    discounts = Discounts.objects.filter(event_id=event_id)
    serializer = DiscountsSerializer(discounts, many=True)
    return Response(serializer.data)


def applyDiscount(discount_code):
    discount = Discounts.objects.get(code=discount_code)
    if discount.quantity_available > 0 and discount.end_date >= datetime.datetime.now():
        discount.quantity_sold += 1
        discount.quantity_available -= 1
        discount.save()
    else:
        return None
