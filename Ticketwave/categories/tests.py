from django.test import TestCase
from .models import Categories
from .serializers import CategoriesSerializer


class CategoriesTest(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(
            id=1,
            name="test-cat",
            short_name="tc",
            resource_uri="test-cat.com",
            parent_category=-1,
        )
        self.subcategory = Categories.objects.create(
            id=2,
            name="test-subcat",
            short_name="tsc",
            resource_uri="test-subcat.com",
            parent_category=1,
        )
        self.serializer = CategoriesSerializer(self.category)

    def test_Categories_Model(self):
        category1 = Categories.objects.get(name="test-cat")
        self.assertEqual(category1.short_name, "tc")

    def test_Categories_Serializer(self):
        data = self.serializer.data
        self.assertEqual(data["name"], "test-cat")

    def test_get_subcategory(self):
        subcategory1 = Categories.objects.get(parent_category=1)
        self.assertEqual(subcategory1.name, "test-subcat")
