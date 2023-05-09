from rest_framework.response import Response
from .models import Categories
from .serializers import CategoriesSerializer
from rest_framework import generics
from rest_framework.decorators import api_view


@api_view(("GET",))
def listCategories(request):
    categories = Categories.objects.all()
    serializer = CategoriesSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(("GET",))
def listSubcategoriesByCategory(request, category_id):
    subcategories = Categories.objects.filter(parent_category=category_id)
    serializer = CategoriesSerializer(subcategories, many=True)
    return Response(serializer.data)


class create(generics.CreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
