from django.urls import path
from rest_framework import routers

from providers.views import ProviderViewSet, ServiceAreaViewSet, ProvidersByServiceAreaLocation

router = routers.DefaultRouter()
router.register(r'', ProviderViewSet)
router.register(r'service_area', ServiceAreaViewSet)

urlpatterns = [
    path('by_service_area_location/', ProvidersByServiceAreaLocation.as_view()),
]

urlpatterns += router.urls
