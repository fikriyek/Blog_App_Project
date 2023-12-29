from rest_framework import permissions

# Permission for PUT, POST, DELETE when User is staff/admin.
class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return bool(request.user and request.user.is_staff)

# Permission for PUT, POST, DELETE when User is staff and owner        
class IsOwnerAndStaffOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        else:
            return bool(request.user.is_staff and (obj.user == request.user))