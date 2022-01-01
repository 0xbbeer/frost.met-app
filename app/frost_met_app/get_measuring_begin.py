import requests
import os
from frost_met_app.models import MeasuringBegin, WindDirection, Stations


def get_begin(self):
    # ID for connect to frost.met API
    client_id = os.environ.get('FROST_API_ID', None)
    client_password = os.environ.get('FROST_API_PASSWORD', None)
    endpoint = 'https://frost.met.no/observations/availableTimeSeries/v0.jsonld'
    parameters = {
        'elements': 'wind_from_direction',
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

        station_id = station_info['sourceId']
        station_id = station_id.split(':')
        station_id = station_id[0]

        validFrom = station_info['validFrom']

        try:
            if Stations.objects.get(station_id=station_id):
                add_dates = MeasuringBegin(
                    station_id=station_id,
                    start_date=validFrom,
                )
                add_dates.save()

        except Exception:
            continue

    # 10 Oldest stations
    ten_stations = MeasuringBegin.objects.all().order_by('start_date')[:10]

    for station in ten_stations:

        station = station.station_id

        try:
            add_station_id = WindDirection(
                station_id=station,
                wind_direction='None'
            )
            add_station_id.save()
        except Exception:
            continue
