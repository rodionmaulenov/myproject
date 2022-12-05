from rest_framework import viewsets
from .models import Document
from .serializer import DocumentSerializer
from persons.mixins import StaffAuthenticatedPermissionMixin


class DocumentView(
    StaffAuthenticatedPermissionMixin,
                   viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
