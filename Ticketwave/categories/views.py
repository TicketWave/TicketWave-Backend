from django.http import JsonResponse
from .models import Categories
from .serializers import CategoriesSerializer

def listCategories(request):
    categories = Categories.objects.all()
    serializer = CategoriesSerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)