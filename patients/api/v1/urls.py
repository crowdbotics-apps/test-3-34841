from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AddressViewSet, PatientViewSet

router = DefaultRouter()
router.register("patient", PatientViewSet)
router.register("address", AddressViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
