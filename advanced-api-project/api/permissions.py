from rest_framework.permission import BasePermission
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET', 'HEAD', 'OPTIONS']  or request.user and request.user.is_staff
    
