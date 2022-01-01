import requests
import os
from frost_met_app.models import Stations
from frost_met_app import get_measuring_begin


def get_stations(self):
    client_id = '38fe8d60-e312-4086-88fd-3201742d387d'
    client_password = os.environ.get('FROST_API_PASSWORD', None)
    endpoint = 'https://frost.met.no/sources/v0.jsonld'
    parameters = {
        'elements': 'wind_from_direction',
        'country': 'Norge',
    }
    # HTTP GET request
    r = requests.get(
        endpoint,
        parameters,
        auth=(
            client_id,
            client_password))
    # Extract JSON data
    json = r.json()
    data = json['data']

    for station_info in data:

        station_id = station_info['id']

        country = station_info['country']

        try:
            station_geometry = station_info['geometry']
            geometry = station_geometry['coordinates']
            # longitude
            W = geometry[1]
            # latitude
            N = geometry[0]
        except Exception:
            geometry = 'None'

        try:
            municipality = station_info['municipality']
        except Exception:
            municipality = "None"

        stationHolders = station_info['stationHolders']
        try:
            stationHolders = stationHolders[0]
        except Exception:
            stationHolders = "None"

        validFrom = station_info['validFrom']

        add_stations = Stations(
            station_id=station_id,
            country=country,
            geometry=geometry,
            municipality=municipality,
            stationholder=stationHolders,
            validfrom=validFrom,
            w=W,
            n=N,
        )
        add_stations.save()

    get_measuring_begin.get_begin('GET')
