import requests
import psycopg2
import os

conn_to_pg = psycopg2.connect(
    dbname=os.environ.get('POSTGRES_DB', None),
    user=os.environ.get('POSTGRES_USER', None),
    password=os.environ.get('POSTGRES_PASSWORD', None),
    host=os.environ.get('POSTGRES_HOST', None))

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
        cursor = conn_to_pg.cursor()
        cursor.execute(
            "insert into frost_met_app_measuringbegin("
            "station_id, start_date) values ("
            "'%s',"
            "'%s');" % (
                station_id, validFrom))
        conn_to_pg.commit()
        cursor.close()
    except:
        continue

# 10 Oldest stations
cursor = conn_to_pg.cursor()
cursor.execute(
    "select station_id from frost_met_app_measuringbegin "
    "order by start_date limit 10")
stations = cursor.fetchall()
conn_to_pg.commit()
cursor.close()

for station in stations:

    station = station[0]

    cursor = conn_to_pg.cursor()
    cursor.execute(
        "insert into frost_met_app_winddirection("
        "station_id) values ("
        "'%s');" % (
            station,))
    conn_to_pg.commit()
    cursor.close()


