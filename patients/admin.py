from django.contrib import admin
from .models import Address, Patient

admin.site.register(Patient)
admin.site.register(Address)

# Register your models here.
