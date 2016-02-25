from rest_framework import permissions


class ViewEditIfAdminOrUser(permissions.BasePermission):
    """
    Custom permission to only allow owners and admin view/edit
    """

    def has_object_permission(self, request, view, obj):
        # Only user or admin may look at user profiles and addresses
        # Try/except used for differentiating between MailingAddress object and
        # User object. For a MailingAddress object the user attribute
        # is referenced for authentication. For a User object the request
        # user is referenced for authentication.
        try:
            # For MailingAddress object and other User related models
            return obj.user == request.user or request.user.is_staff
        except:
            # For User object
            return obj == request.user or request.user.is_staff
        return False