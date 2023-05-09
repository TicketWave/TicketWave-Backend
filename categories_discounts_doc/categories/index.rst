Categories
==========

API Documentation
-----------------

.. py:function:: listCategories(request)
   
   List all categories.
   
   This function-based view retrieves all categories.
   
   :param request: The HTTP request object.
   :return: A response containing the serialized data of all categories.
   :rtype: Response

.. py:function:: listSubcategoriesByCategory(request, category_id)
   
   List subcategories by category ID.
   
   This function-based view retrieves all subcategories associated with the given category ID.
   
   :param request: The HTTP request object.
   :param category_id: The ID of the category to filter subcategories by.
   :type category_id: int
   :return: A response containing the serialized data of the subcategories.
   :rtype: Response


Model Documentation
-------------------

.. py:class:: Categories(models.Model)
   
   Model for categories.
   
   :ivar id: The ID of the category. (AutoField)
   :ivar name: The name of the category. (CharField, max_length=64, unique=True)
   :ivar short_name: The short name of the category. (CharField, max_length=18, unique=True)
   :ivar resource_uri: The URL of the resource associated with the category. (URLField, blank=True, null=True)
   :ivar parent_category: The ID of the parent category. (IntegerField, blank=True, null=True)
