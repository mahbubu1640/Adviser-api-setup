from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertiserViewSet, LocationViewSet, AdSpendViewSet, BusinessCryptoViewSet

router = DefaultRouter()
router.register(r'advertisers', AdvertiserViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'adspend', AdSpendViewSet)
router.register(r'businesscrypto', BusinessCryptoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
