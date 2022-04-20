from rest_framework import serializers
from patients.models import Address, Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
