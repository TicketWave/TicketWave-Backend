from rest_framework import permissions
from rest_framework.request import Request
from django.core.exceptions import ObjectDoesNotExist


class Is_eventowner_or_readonly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request: Request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            # Write permissions are only allowed to the owner of the snippet.
            # obj."user" (OWNER) NEEDS TO BE DEFINED FOR event
            return obj.owner == request.user
        except:
            return False
        
class Is_eventowner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view/read it.
    """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        if request.user.is_authenticated:
            try:
                return obj.owner == request.user
            except:
                return False
        else: return False
        
class Is_orderowner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view/read it.
    """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        if request.user.is_authenticated:
            try:
                return obj.user_id == request.user
            except:
                return False
        else: return False
        
class Is_venueowner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view/read it.
    """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        
        if request.user.is_authenticated:
            try:
                return obj.event.owner_id == request.user.id
            except ObjectDoesNotExist:
                return False
        else: return False