from rest_framework import permissions
from .permissions import StaffModelPermission


class StaffAuthenticatedPermissionMixin:
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser, StaffModelPermission]
