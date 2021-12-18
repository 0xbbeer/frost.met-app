import requests
import psycopg2
import os


# DB Credentials
conn_to_pg = psycopg2.connect(
    dbname=os.environ.get('POSTGRES_DB', None),
    user=os.environ.get('POSTGRES_USER', None),
    password=os.environ.get('POSTGRES_PASSWORD', None),
    host=os.environ.get('POSTGRES_HOST', None))

# ID for connect to frost.met API
client_id = '38fe8d60-e312-4086-88fd-3201742d387d'
client_password = os.environ.get('FROST_API_PASSWORD', None)
cursor = conn_to_pg.cursor()
cursor.execute(
    "select station_id from frost_met_app_winddirection")
stations = cursor.fetchall()
conn_to_pg.commit()
cursor.close()

for station in stations:
    station = station[0]
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
            except:
                wind_from_direction = 'NO DATA'

            cursor = conn_to_pg.cursor()
            cursor.execute(
                "update frost_met_app_winddirection set wind_direction = ("
                "'%s')  where station_id = ('%s');" % (
                    wind_from_direction, station))
            conn_to_pg.commit()
            cursor.close()

    except:
        continue
