import requests
import sqlite3

from citibike.entities.region import RegionDb, Region

station_information = []

"""
"feeds": [
{
"name": "system_alerts",
"url": "https://gbfs.citibikenyc.com/gbfs/en/system_alerts.json"
},
{
"name": "station_status",
"url": "https://gbfs.citibikenyc.com/gbfs/en/station_status.json"
},
{
"name": "system_information",
"url": "https://gbfs.citibikenyc.com/gbfs/en/system_information.json"
},
{
"name": "system_regions",
},
"url": "https://gbfs.citibikenyc.com/gbfs/en/system_regions.json"
{
"name": "station_information",
"url": "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"
}
]
"""



### THIS IS FOR REGION IMPORTS
resp = requests.get('https://gbfs.citibikenyc.com/gbfs/en/system_regions.json')
data = resp.json()['data']['regions']

rdb = RegionDb()
for datum in data:
    instance = Region()
    for key, value in datum.items():
        if hasattr(instance, key):
            setattr(instance, key, value)
        station_information.append(instance)
    rdb.insert_region(instance)


### THIS IS FOR STATION IMPORTS
# resp = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_information.json')
# data = resp.json()['data']['stations']
#
# sdb = StationDb()
# for datum in data:
#     instance = Station()
#     for key, value in datum.items():
#         if hasattr(instance, key):
#             setattr(instance, key, value)
#         station_information.append(instance)
#     sdb.insert_station(instance)


