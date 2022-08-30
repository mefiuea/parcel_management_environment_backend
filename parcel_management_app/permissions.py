from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        print('SAFE METHODS: ', permissions.SAFE_METHODS, flush=True)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post
        return obj.author == request.user


class NoAdminUser(permissions.BasePermission):
    """
    No admin user can see only own objects and add new objects.
    """

    # def has_permission(self, request, view):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
