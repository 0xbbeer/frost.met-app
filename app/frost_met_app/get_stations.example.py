import requests
import psycopg2
import os


conn_to_pg = psycopg2.connect(
    dbname='[FROST_DB_NAME]',
    user='[FROST_DB_USER]',
    password='[FROST_DB_PASSWORD]',
    host='[FROST_DB_HOST]')

client_id = '[FROST_API_ID]'

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
        '[FROST_API_PASSWORD]'))
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
    except:
        geometry = 'None'

    try:
        municipality = station_info['municipality']
    except:
        municipality = "None"

    stationHolders = station_info['stationHolders']
    try:
        stationHolders = stationHolders[0]
    except:
        stationHolders = "None"

    validFrom = station_info['validFrom']

    cursor = conn_to_pg.cursor()
    cursor.execute(
        "insert into frost_met_app_stations("
        "station_id,"
        "country,"
        "geometry,"
        "municipality, "
        "stationHolder, "
        "validFrom, "
        "w, "
        "n) values ("
        "'%s',"
        "'%s',"
        "'%s',"
        "'%s',"
        "'%s',"
        "'%s',"
        "'%s',"
        "'%s');" % (
            station_id, country, geometry,
            municipality, stationHolders, validFrom, W, N))
    conn_to_pg.commit()
    cursor.close()

os.system('python3.9 frost_met_app/get_measuring_begin.py')
