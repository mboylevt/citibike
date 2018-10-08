import requests

from citibike.entities.station import Station, StationDb

station_list = []
resp = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_information.json')
data = resp.json()['data']['stations']

for datum in data:
    instance = Station()
    for key, value in datum.items():
        if hasattr(instance, key):
            setattr(instance, key, value)
            station_list.append(instance)

for station in station_list:
    try:
        test_stn = StationDb().get_station_by_id(station.station_id)
    except RuntimeError:
        StationDb().insert_station(station)
