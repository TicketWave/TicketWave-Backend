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
        
@api_view(['GET', 'PUT', 'DELETE'])
def addDelUpDiscount(request, id):
    
    try:
        discount = Discounts.objects.get(pk=id)
    except Discounts.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DiscountsSerializer(discount)
        return Response(data= serializer.data, status= status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = DiscountsSerializer(discount, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        discount.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
