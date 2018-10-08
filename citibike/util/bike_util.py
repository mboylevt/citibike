import requests
from citibike.entities.region import RegionDb
from citibike.entities.station import StationDb, Station
from citibike.entities.station_status import StationStatus


class RegionStatus():
    def __init__(self):
        self.num_bikes_available = 0
        self.num_ebikes_available = 0
        self.num_bikes_disabled = 0
        self.num_docks_available = 0
        self.num_docks_disabled = 0


def __get_stations():
    '''

    :return:
    :rtype: [Station]
    '''


def __get_station_status():
    '''

    :return:
    :rtype: [StationStatus]
    '''
    station_status_list = []
    resp = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')
    data = resp.json()['data']['stations']

    for datum in data:
        instance = StationStatus()
        for key, value in datum.items():
            if hasattr(instance, key):
                setattr(instance, key, value)
        station_status_list.append(instance)
    return station_status_list

def __init_region_map():
    regions = RegionDb().get_all_regions()
    region_map = {}
    for region in regions:
        region_map[region.name] = []
    return region_map

def get_ebikes():

    station_status_list = __get_station_status()
    region_map = __init_region_map()

    for status in station_status_list:
        if status.num_ebikes_available > 0:
            stn = StationDb().get_station_by_id(status.station_id)
            rgn = RegionDb().get_region_by_id(stn.region_id)
            region_map[rgn.name].append((stn, status))
    return region_map

def get_region_status():
    '''

    :rtype: [RegionStatus]
    '''
    station_status_list = __get_station_status()
    region_map = __init_region_map()
    for region in region_map:
        region_map[region] = RegionStatus()

    for station_status in station_status_list:
        stn = StationDb().get_station_by_id(station_status.station_id)
        rgn = RegionDb().get_region_by_id(stn.region_id)
        region_map[rgn.name].num_bikes_available += station_status.num_bikes_available
        region_map[rgn.name].num_ebikes_available += station_status.num_ebikes_available
        region_map[rgn.name].num_bikes_disabled += station_status.num_bikes_disabled
        region_map[rgn.name].num_docks_available += station_status.num_docks_available
        region_map[rgn.name].num_docks_disabled += station_status.num_docks_disabled

    return region_map