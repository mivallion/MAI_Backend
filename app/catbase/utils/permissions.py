from rest_framework import permissions


class IsGetOrIsAuthenticated(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'GET':
            return True

        return (request.user and obj.user_id is None) or (request.user == obj.user_id) and request.user.is_authenticated
