from rest_framework import viewsets
from .models import Limit
from .serializers import LimitSerializer
from persons.mixins import StaffAuthenticatedPermissionMixin


class limitView(
    StaffAuthenticatedPermissionMixin,
                viewsets.ModelViewSet):
    queryset = Limit.objects.all()
    serializer_class = LimitSerializer
