from .models import Discounts
from .serializers import DiscountsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def manageDiscounts(request):
    if request.method == 'GET':
        discounts = Discounts.objects.all()
        serializer = DiscountsSerializer(discounts, many=True)
        return Response({'discounts': serializer.data})
    
    if request.method == 'POST':
        serializer = DiscountsSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status= status.HTTP_201_CREATED)