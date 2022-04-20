from rest_framework import authentication
from diagnostics.models import Patient
from .serializers import PatientSerializer
from rest_framework import viewsets


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Patient.objects.all()
