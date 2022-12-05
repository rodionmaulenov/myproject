from rest_framework import viewsets, filters
from .mixins import StaffAuthenticatedPermissionMixin
from .models import Person
from .serializers import PersonSerializer


class PersonView(
    StaffAuthenticatedPermissionMixin,
                 viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['-date_create']
    filterset_fields = ['name', 'surname']

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

