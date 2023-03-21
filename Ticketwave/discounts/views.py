from django.http import JsonResponse
from .models import Discounts
from .serializers import DiscountsSerializer

def listDiscounts(request):
    discounts = Discounts.objects.all()
    serializer = DiscountsSerializer(discounts, many=True)
    return JsonResponse(serializer.data, safe=False)