from django.conf import settings
from django.db import models


class Patient(models.Model):
    "Generated Model"
    givenName = models.CharField(
        max_length=256,
    )
    familyName = models.CharField(
        max_length=256,
    )
    gender = models.CharField(
        max_length=8,
    )
    dateOfBirth = models.DateField()
    socialSecurityNumber = models.CharField(
        max_length=16,
    )
    address = models.ForeignKey(
        "patients.Address",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="patient_address",
    )


class Address(models.Model):
    "Generated Model"
    line1 = models.CharField(
        max_length=256,
    )
    line2 = models.CharField(
        max_length=256,
    )
    city = models.CharField(
        max_length=256,
    )
    stateCode = models.CharField(
        max_length=4,
    )
    zipCode = models.CharField(
        max_length=16,
    )
    countryCode = models.CharField(
        max_length=4,
    )


# Create your models here.
