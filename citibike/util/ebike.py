import requests
from citibike.entities.region import RegionDb
from citibike.entities.station import StationDb
from citibike.entities.station_status import StationStatus


def get_ebikes():
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
            stn = StationDb().get_station_by_id(status.station_id)
            rgn = RegionDb().get_region_by_id(stn.region_id)
            region_map[rgn.name].append((stn, status))
            ebike_available += status.num_ebikes_available

    return region_map