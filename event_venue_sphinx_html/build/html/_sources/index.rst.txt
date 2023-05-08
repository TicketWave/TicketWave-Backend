.. events_functional_doc documentation master file, created by
   sphinx-quickstart on Tue Apr 18 20:02:34 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to events_functional_doc's documentation!
=================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

API Reference
-------------

event_follower_count
~~~~~~~~~~~~~~~~~~~~~~~~~~~
… py:attribute:: permission_classes

  A list of permission classes for the view. In this case, it is set to `[AllowAny]`, which means that any user can access the view, even if they are not authenticated.

- ``get(request, event_id)``

  Handles `GET` requests to the view.

  :param request: The request object.
  :type request: :class:`django.http.HttpRequest`
  :param event_id: The ID of the event to retrieve the follower count for.
  :type event_id: int
  :returns: A response object with a dictionary containing the follower count of the event.
  :rtype: :class:`rest_framework.response.Response`

  When a `GET` request is made to this view with a valid `event_id`, the view attempts to retrieve an `Event` object with the given `event_id`. If no such event exists, the view returns a response with a `404` status code.

  If the event exists, the view retrieves the follower count of the event by calling the `count` method on the `followers` attribute of the `Event` object. The follower count is returned in a dictionary in the response.

follow_event
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Django API view that allows authenticated users to follow an event.

py:attribute:: permission_classes

A list of permission classes for the view. In this case, it is set to `[IsAuthenticated]`, which means that only authenticated users can access the view.

- ``post(request, event_id)``

  Handles `POST` requests to the view.

  :param request: The request object.
  :type request: :class:`django.http.HttpRequest`
  :param event_id: The ID of the event to follow.
  :type event_id: int
  :returns: A response object.
  :rtype: :class:`rest_framework.response.Response`

  When a `POST` request is made to this view with a valid `event_id`, the view checks if the user is authenticated. If the user is not authenticated, the view returns a response with a `401` status code.

  If the user is authenticated, the view attempts to retrieve an `Event` object with the given `event_id`. If no such event exists, the view returns a response with a `404` status code.

  If the event exists, the view adds the user to the event's followers and returns a response with a `200` status code.

- ``delete(request, event_id)``

  Handles `DELETE` requests to the view.

  :param request: The request object.
  :type request: :class:`django.http.HttpRequest`
  :param event_id: The ID of the event to unfollow.
  :type event_id: int
  :returns: A response object.
  :rtype: :class:`rest_framework.response.Response`

  When a `DELETE` request is made to this view with a valid `event_id`, the view checks if the user is authenticated. If the user is not authenticated, the view returns a response with a `401` status code.

  If the user is authenticated, the view attempts to retrieve an `Event` object with the given `event_id`. If no such event exists, the view returns a response with a `404` status code.

  If the event exists, the view removes the user from the event's followers and returns a response with a `200` status code.



event_increment_view_counter
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Django API view that increments the view counter of an event.

… py:attribute:: serializer_class

  The serializer class for the view. In this case, it is set to `IncrementViewSerializer`.
… py:attribute:: queryset

  The queryset for the view. In this case, it is set to `Event.objects.all()`, which means that all events are available for incrementing their view counter.
… py:attribute:: permission_classes

  A list of permission classes for the view. In this case, it is set to `[AllowAny]`, which means that any user can access the view, even if they are not authenticated.

- ``patch(request, *args, **kwargs)``

  Handles `PATCH` requests to the view.

  :param request: The request object.
  :type request: :class:`django.http.HttpRequest`
  :param args: Additional positional arguments.
  :param kwargs: Additional keyword arguments.
  :returns: A response object with the serialized data of the updated event.
  :rtype: :class:`rest_framework.response.Response`

  When a `PATCH` request is made to this view with a valid event ID in the URL, the view retrieves the corresponding `Event` object and increments its `view_counter` attribute by 1.
   The updated event is then saved and serialized using the `IncrementViewSerializer` class. The serialized data is returned in the response.

event_unpublish
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Django API view that unpublishes an event.

… py:attribute:: permission_classes

  A list of permission classes for the view. In this case, it is set to `[IsAuthenticated, Is_eventowner]`, which means that only authenticated users who are also the owner of the event can access the view.

- ``get(request, event_id)``

  Handles `GET` requests to the view.

  :param request: The request object.
  :type request: :class:`django.http.HttpRequest`
  :param event_id: The ID of the event to unpublish.
  :type event_id: int
  :returns: A response object with a dictionary indicating whether the event was unpublished or not.
  :rtype: :class:`rest_framework.response.Response`

  When a `GET` request is made to this view with a valid `event_id`, the view attempts to retrieve an `Event` object with the given `event_id`. If no such event exists or if an error occurs, the view returns a response with a `400` status code.

  If the event exists, the view calls the `check_order_status` function with the `Event` object as an argument. If the result of this function is `True`, the view updates the `status` and `publish` attributes of the `Event` object to `'canceled'` and `False`, respectively, using a serializer. The updated event is then saved and a response with a dictionary indicating that the event was unpublished is returned.

  If the result of the `check_order_status` function is not `True`, a response with a dictionary indicating that the event was not unpublished is returned.


event_publish
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Django API view that publishes an event.

… py:attribute:: permission_classes

  A list of permission classes for the view. In this case, it is set to `[IsAuthenticated, Is_eventowner]`, which means that only authenticated users who are also the owner of the event can access the view.

- ``get(request, event_id)``

  Handles `GET` requests to the view.

  :param request: The request object.
  :type request: :class:`django.http.HttpRequest`
  :param event_id: The ID of the event to publish.
  :type event_id: int
  :returns: A response object with a dictionary indicating whether the event was published or not.
  :rtype: :class:`rest_framework.response.Response`

  When a `GET` request is made to this view with a valid `event_id`, the view attempts to retrieve an `Event` object with the given `event_id`. If no such event exists or if an error occurs, the view returns a response with a `400` status code.

  If the event exists, the view calls the `check_publish_requirements` function with the `Event` object as an argument. The view also retrieves several values from the request data: `'published'`, `'published'`, and `'password'`.

  If all these values are not `None` and if the result of the `check_publish_requirements` function is `True`, the view updates several attributes of the `Event` object using a serializer. The updated attributes are `'status'`, `'publish'`, `'start'`, `'end'`, and `'password'`. The updated values are `'live'`, `True`, and the values retrieved from the request data, respectively. The updated event is then saved and a response with a dictionary indicating that the event was published is returned.

  If any of these values are `None` or if the result of the `check_publish_requirements` function is not `True`, a response with a dictionary indicating that


event_copy
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Django API view that creates a copy of an event.

… py:attribute:: permission_classes

  A list of permission classes for the view. In this case, it is set to `[IsAuthenticated, Is_eventowner]`, which means that only authenticated users who are also the owner of the event can access the view.

- ``get(request, event_id)``

  Handles `GET` requests to the view.

  :param request: The request object.
  :type request: :class:`django.http.HttpRequest`
  :param event_id: The ID of the event to copy.
  :type event_id: int
  :returns: A response object with a dictionary indicating whether the event was copied or not.
  :rtype: :class:`rest_framework.response.Response`

  When a `GET` request is made to this view with a valid `event_id`, the view attempts to retrieve an `Event` object with the given `event_id`. If no such event exists or if an error occurs, the view returns a response with a `400` status code and a dictionary indicating that the event was not copied.

  If the event exists, the view creates a copy of the `Event` object by setting its primary key (`pk`) to `None` and calling its `save` method. This creates a new `Event` object in the database with the same data as the original `Event` object. The view then returns a response with a dictionary indicating that the event was copied.

check_order_status(event)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Checks if an event has any pending or completed orders.

:param event: The event to check. :type event: :class:Event :returns: False if the event has any pending or completed orders, True otherwise. :rtype: bool

This function retrieves all Order objects associated with the given event by calling the filter method on the Order model’s manager with the event argument set to the given event.

The function then iterates over the retrieved Order objects and checks their status attribute. If any of the Order objects have a status of 'pending' or 'completed', the function returns False.

If none of the Order objects have a status of 'pending' or 'completed', the function returns True.

check_publish_requirements(event)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Checks if an event meets the requirements for being published.

:param event: The event to check. :type event: :class:Event :returns: False if the event does not meet the requirements for being published, True otherwise. :rtype: bool

This function checks if the given event has a non-empty name and description. If either of these attributes is an empty string, the function returns False.

it also checks that the event has a ticket created for it.


event_price
===========

.. autoclass:: event_price
    :members:

This class defines an API view for retrieving the ticket prices for a given event.

The view allows any user to access it and only supports GET requests.

GET request
-----------

Sends a GET request to retrieve the ticket prices for a given event.

:param event_id: The ID of the event to retrieve ticket prices for.
:type event_id: int
:returns: A JSON response containing the ticket prices for the given event, or an error response if the request fails.
:rtype: JSON response

Example usage::

    # Send a GET request to retrieve ticket prices for event with ID 1
    response = requests.get('/event_price/1/')
    # Check the response status code
    print(response.status_code)  # 200
    # Parse the JSON response
    data = response.json()
    # Print the ticket prices
    print(data['ticket_price'])


event_sales_total
=================

.. autoclass:: event_sales_total
    :members:

This class defines an API view for retrieving the total sales for a given event.

The view only supports GET requests.

GET request
-----------

Sends a GET request to retrieve the total sales for a given event.

:param event_id: The ID of the event to retrieve total sales for.
:type event_id: int
:returns: A JSON response containing the total sales for the given event, or an error response if the request fails.
:rtype: JSON response

Example usage::

    # Send a GET request to retrieve total sales for event with ID 1
    response = requests.get('/event_sales_total/1/')
    # Check the response status code
    print(response.status_code)  # 200
    # Parse the JSON response
    data = response.json()
    # Print the total sales
    print(data['total sales'])


sales_by_ticket
===============

.. autoclass:: sales_by_ticket
    :members:

This class defines an API view for retrieving the sales and amount of tickets sold by ticket type for a given event.

The view only supports GET requests.

GET request
-----------

Sends a GET request to retrieve the sales and amount of tickets sold by ticket type for a given event.

:param event_id: The ID of the event to retrieve sales and amount of tickets sold by ticket type for.
:type event_id: int
:returns: A JSON response containing the sales and amount of tickets sold by ticket type for the given event, or an error response if the request fails.
:rtype: JSON response

Example usage::

    # Send a GET request to retrieve sales and amount of tickets sold by ticket type for event with ID 1
    response = requests.get('/sales_by_ticket/1/')
    # Check the response status code
    print(response.status_code)  # 200
    # Parse the JSON response
    data = response.json()
    # Print the sales and amount of tickets sold by ticket type
    print(data['sales'])
    print(data['amount'])


event_amount_tickets_sold
=========================

.. autoclass:: event_amount_tickets_sold
    :members:

This class defines an API view for retrieving the total amount of tickets sold for a given event.

The view only supports GET requests.

GET request
-----------

Sends a GET request to retrieve the total amount of tickets sold for a given event.

:param event_id: The ID of the event to retrieve the total amount of tickets sold for.
:type event_id: int
:returns: A JSON response containing the total amount of tickets sold for the given event, or an error response if the request fails.
:rtype: JSON response

Example usage::

    # Send a GET request to retrieve the total amount of tickets sold for event with ID 1
    response = requests.get('/event_amount_tickets_sold/1/')
    # Check the response status code
    print(response.status_code)  # 200
    # Parse the JSON response
    data = response.json()
    # Print the total amount of tickets sold
    print(data['tickets sold'])

get_location_info
=================

.. autofunction:: get_location_info

This function takes in a latitude and longitude and returns the city, state, and country of the location.

:param latitude: The latitude of the location.
:type latitude: float
:param longitude: The longitude of the location.
:type longitude: float
:returns: A tuple containing the city, state, and country of the location.
:rtype: tuple

Example usage::

    >>> from geopy.geocoders import Nominatim
    >>> city, state, country = get_location_info(51.5074, 0.1278)
    >>> print(city)
    London
    >>> print(state)
    England
    >>> print(country)
    United Kingdom


