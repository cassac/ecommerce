from rest_framework import permissions


class ViewIfAdminOrSelf(permissions.BasePermission):
    """
    Custom permission to only allow admin or self to view
    """

    def has_permission(self, request, view):
        # Can only view asset if belongs to user or user is admin
        return request.user.id == int(view.kwargs['pk']) or request.user.is_staff


class EditIfAdminOrSelf(permissions.BasePermission):
    """
    Custom permission to only allow admin or self to edit
    """
    def has_permission(self, request, view):
        # Must be staff or authenticated user, then has_object_permission
        # Will check if user is the owner of the object
        return request.user.is_staff or not request.user.is_anonymous()

    def has_object_permission(self, request, view, obj):
        # User must be an admin or owns the object
        return obj.user == request.user or request.user.is_staff