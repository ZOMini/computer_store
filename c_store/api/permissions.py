from rest_framework import permissions


class AdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        # print(request.user.has_perm('store.add_item', obj=None))
        return (
            request.method in permissions.SAFE_METHODS
            or bool(request.user and request.user.is_staff)
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or bool(request.user and request.user.is_staff)
        )
