from rest_framework import permissions


class IsAdminOrRegularUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Write and read permissions for all parcels are allowed to admin
        # For no admin user write and read permissions are allowed only if user is creator of object
        if bool(request.user and request.user.is_staff and request.user.is_admin):
            return True
        else:
            return obj.owner == request.user
