from rest_framework import authentication
from patients.models import Address, Patient
from .serializers import AddressSerializer, PatientSerializer
from rest_framework import viewsets


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Patient.objects.all()


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Address.objects.all()
