
# Create your models here.
from django.db import models


class Advertiser(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        return self.name

class AdSpend(models.Model):
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    def __str__(self):
        return self.amount

class BusinessCrypto(models.Model):
    name = models.CharField(max_length=100)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    def __str__(self):
        return self.name
    
