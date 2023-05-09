Discounts
=========

API Documentation
-----------------

.. py:class:: manageDiscounts(generics.RetrieveUpdateDestroyAPIView)
   
   API view for managing a discount.
   
   
   This class-based view allows retrieving, updating, and deleting a discount based on its ID.
   
   :ivar serializer_class: The serializer class to use for the discount.
   :ivar queryset: The queryset containing all discounts.
   :ivar lookup_field: The field to use as the lookup parameter when retrieving a discount.

.. py:class:: createDiscount(generics.CreateAPIView)
   
   API view for creating a discount.
   
   This class-based view allows creating a new discount.
   
   :ivar serializer_class: The serializer class to use for the discount.
   :ivar queryset: The queryset containing all discounts.

.. py:function:: listDiscountsByEvent(request, event_id)
   
   Retrieve a list of discounts by event ID.
   
   This function-based view retrieves a list of discounts associated with the given event ID.
   
   :param request: The HTTP request object.
   :param event_id: The ID of the event to filter discounts by.
   :type event_id: int
   :return: A response containing the serialized data of the discounts.
   :rtype: Response

.. py:function:: applyDiscount(discount_code)
   
   Apply a discount with the given discount code.
   
   This function applies a discount to a purchase based on the provided discount code.
   It updates the quantity sold and available if the discount is valid and available.
   
   :param discount_code: The discount code to apply.
   :type discount_code: str
   :return: None if the discount is not valid or available, otherwise, no explicit return value.

Model Documentation
-------------------

.. py:class:: Discounts(models.Model)

   Model for discounts.

   :ivar code: The discount code. (CharField, max_length=20, unique=True, blank=False, primary_key=True)
   :ivar type: The type of the discount. (CharField, max_length=255)
   :ivar end_date: The end date of the discount. (DateTimeField, blank=False)
   :ivar start_date: The start date of the discount. (DateTimeField, blank=False)
   :ivar percent_off: The percentage off for the discount. (FloatField)
   :ivar quantity_available: The quantity of the discount available. (IntegerField)
   :ivar quantity_sold: The quantity of the discount sold. (IntegerField)
   :ivar event_id: The foreign key to the Event model. (ForeignKey to Event, on_delete=models.CASCADE)
