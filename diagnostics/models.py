from django.conf import settings
from django.db import models


class Patient(models.Model):
    "Generated Model"
    lastName = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    givenName = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=32,
        null=True,
        blank=True,
    )
    dateOfBirth = models.DateField(
        null=True,
        blank=True,
    )
    socialSecurityNumber = models.CharField(
        max_length=16,
        null=True,
        blank=True,
    )


# Create your models here.
