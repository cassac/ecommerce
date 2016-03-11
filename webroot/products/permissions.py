from rest_framework import permissions

class EditIfIsAdminUser(permissions.BasePermission):
    """
    Custom permission to only allow user or admin to edit
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        return request.user.is_staff