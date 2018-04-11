from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the owners of an object to edit i
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, Head or OPTIONS requests.

        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user