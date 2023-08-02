from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True

        return False


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff == True:
            return True

        return False


class IsStaffCreate(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff == True:
            return False

        return True
