
from rest_framework import viewsets
from .models import Advertiser, Location, AdSpend, BusinessCrypto
from .serializers import AdvertiserSerializer, LocationSerializer, AdSpendSerializer, BusinessCryptoSerializer

class AdvertiserViewSet(viewsets.ModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class AdSpendViewSet(viewsets.ModelViewSet):
    queryset = AdSpend.objects.all()
    serializer_class = AdSpendSerializer

class BusinessCryptoViewSet(viewsets.ModelViewSet):
    queryset = BusinessCrypto.objects.all()
    serializer_class = BusinessCryptoSerializer
