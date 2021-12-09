from django.db import models


# All Norway Meteostations
#
# Get from 'https://frost.met.no/sources/v0.jsonld'
class Stations(models.Model):
    station_id = models.CharField(default="", max_length=512, blank=True, primary_key=True, unique=True)
    country = models.CharField(default="", max_length=512, blank=True)
    geometry = models.CharField(default="", max_length=512, blank=True)
    municipality = models.CharField(default="", max_length=512, blank=True)
    stationholder = models.CharField(default="-", max_length=512, blank=True)
    validfrom = models.DateTimeField(default="", blank=True)
    w = models.CharField(default="", max_length=512, blank=True)
    e = models.CharField(default="", max_length=512, blank=True)

    def __str__(self):
        return self.station_id


# Dates of wind direction measuring began
#
# Get from 'https://frost.met.no/observations/availableTimeSeries/v0.jsonld'
class MeasuringBegin(models.Model):
    station = models.ForeignKey('Stations', to_field='station_id', blank=True, null=True,
                                on_delete=models.CASCADE)
    start_date = models.DateTimeField(default="", blank=True)

    def __str__(self):
        return self.station_id


# Current wind direction values on top 10 oldest meteostations
#
# Get from 'https://frost.met.no/observations/v0.jsonld'
class WindDirection(models.Model):
    station = models.ForeignKey('Stations', to_field='station_id', blank=True, null=True,
                                on_delete=models.CASCADE)
    wind_direction = models.CharField(default="NO DATA", max_length=512, blank=True, null=True)

    def __str__(self):
        return self.station_id
