from rest_framework import permissions
from rest_framework.request import Request


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
            return obj.user  == request.user  #obj."user" (OWNER) NEEDS TO BE DEFINED FOR event
        except:
            return False
    