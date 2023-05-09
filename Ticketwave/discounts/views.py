from .models import Discounts
from .serializers import DiscountsSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime


class manageDiscounts(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiscountsSerializer
    queryset = Discounts.objects.all()
    lookup_field = "code"


class createDiscount(generics.CreateAPIView):
    serializer_class = DiscountsSerializer
    queryset = Discounts.objects.all()


@api_view(("GET",))
def listDiscountsByEvent(request, event_id):
    discounts = Discounts.objects.filter(event_id=event_id)
    serializer = DiscountsSerializer(discounts, many=True)
    return Response(serializer.data)


@api_view(("GET",))
def checkDiscount(request, discount_code):
    try:
        discount = Discounts.objects.get(code=discount_code)
        serializer = DiscountsSerializer(discount)
        return Response(serializer.data, status=200)
    except:
        return Response(status=400)


@api_view(("GET",))
def applyDiscount(discount_code):
    try:
        discount = Discounts.objects.get(code=discount_code)
        if (
            discount.quantity_available > 0
            and discount.end_date >= datetime.datetime.now()
        ):
            discount.quantity_sold += 1
            discount.quantity_available -= 1
            discount.save()
            return Response(status=200)
        else:
            return None
    except:
        return Response(status=400)
