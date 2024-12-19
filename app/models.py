from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)  # Name of the location
    city = models.CharField(max_length=255)  # City where the location is
    lat = models.FloatField()  # Latitude
    lng = models.FloatField()  # Longitude
    created = models.DateTimeField(auto_now_add=True)  # Automatically sets the creation time