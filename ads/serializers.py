from rest_framework import serializers
from .models import Advertiser, Location, AdSpend, BusinessCrypto


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = ['id', 'name', 'logo']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class AdSpendSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdSpend
        fields = '__all__'

class BusinessCryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCrypto
        fields = '__all__'
