from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS or (
                request.user.is_authenticated
                and (request.user.is_admin or request.user.is_superuser)))


class IsAuthorOrAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or request.user.is_admin
                or obj.author == request.user)
