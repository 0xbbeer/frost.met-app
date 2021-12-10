import requests
import psycopg2

conn_to_pg = psycopg2.connect(
    dbname='[FROST_DB_NAME]',
    user='[FROST_DB_USER]',
    password='[FROST_DB_PASSWORD]',
    host='[FROST_DB_HOST]')

# ID for connect to frost.met API
client_id = '[FROST_API_ID]'

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
        '[FROST_API_PASSWORD]'))
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
    except Exception:
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
