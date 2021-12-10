import requests
import psycopg2

# DB Credentials
conn_to_pg = psycopg2.connect(
    dbname='[FROST_DB_NAME]',
    user='[FROST_DB_USER]',
    password='[FROST_DB_PASSWORD]',
    host='[FROST_DB_HOST]')

# ID for connect to frost.met API
client_id = '[FROST_API_ID]'

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
            client_id, '[FROST_API_PASSWORD]'))
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

            cursor = conn_to_pg.cursor()
            cursor.execute(
                "update frost_met_app_winddirection set wind_direction = ("
                "'%s')  where station_id = ('%s');" % (
                    wind_from_direction, station))
            conn_to_pg.commit()
            cursor.close()

    except Exception:
        continue
