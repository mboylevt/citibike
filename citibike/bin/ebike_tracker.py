import requests
from citibike.util import distance
from citibike.entities.region import RegionDb
from citibike.entities.station import StationDb
from citibike.entities.station_status import StationStatus

PAS_LATLONG = (40.7436572, -73.9854901,17)
station_status_list = []

resp = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')
data = resp.json()['data']['stations']
ebike_available = 0

for datum in data:
    instance = StationStatus()
    for key, value in datum.items():
        if hasattr(instance, key):
            setattr(instance, key, value)
    station_status_list.append(instance)

regions = RegionDb().get_all_regions()
region_map = {}
for region in regions:
    region_map[region.name] = []

for status in station_status_list:
    if status.num_ebikes_available > 0:
        stn = StationDb().get_station_by_id(status)
        rgn = RegionDb().get_region_by_id(stn.region_id)
        region_map[rgn.name].append((stn, status))
        ebike_available += status.num_ebikes_available

print("{} ebikes available citiwide".format(ebike_available))
for region, stations in region_map.items():
    print("{}: {} bikes".format(region, len(stations)))
    for station, status in stations:
        dist = distance.get_distance(PAS_LATLONG, (station.lat, station.lon))
        print("\t{name}: {num} bikes, {dist:.2f}m away".format(name=station.name, num=status.num_ebikes_available, dist=dist))