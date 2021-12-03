from django.db import models


class Stations(models.Model):
    station_id = models.CharField(default="", max_length=512, blank=True)
    country = models.CharField(default="", max_length=512, blank=True)
    geometry = models.CharField(default="", max_length=512, blank=True)
    municipality = models.CharField(default="", max_length=512, blank=True)
    stationholder = models.CharField(default="-", max_length=512, blank=True)
    validfrom = models.DateTimeField(default="", blank=True)

    def __str__(self):

        return self.station_id

