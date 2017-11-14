from rest_framework import permissions

__all__=[
    'IsAuthorOrReadOnly',
]

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.author