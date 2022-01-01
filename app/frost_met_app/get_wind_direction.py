import requests
import os
from frost_met_app.models import WindDirection


def wind_direction(self):
    # ID for connect to frost.met API
    client_id = '38fe8d60-e312-4086-88fd-3201742d387d'
    client_password = os.environ.get('FROST_API_PASSWORD', None)

    stations = WindDirection.objects.all()

    for station in stations:
        station = station.station_id

        endpoint = 'https://frost.met.no/observations/v0.jsonld'
        parameters = {
            'sources': station,
            'referencetime': 'latest',
            'elements': 'wind_from_direction'

        }
        # HTTP GET request
        r = requests.get(
            endpoint,
            parameters,
            auth=(
                client_id, client_password))
        # Extract JSON data
        json = r.json()

        try:
            data = json['data']

            for wind_info in data:

                try:
                    observations = wind_info['observations']
                    observations = observations[0]
                    wind_from_direction = observations['value']

                except Exception:
                    wind_from_direction = 'NO DATA'

                s = WindDirection.objects.get(station_id=station)
                s.wind_direction = wind_from_direction

                s.save(update_fields=["wind_direction"])


        except Exception:
            continue
