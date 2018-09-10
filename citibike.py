import requests
import sqlite3

from citibike.entities.station import Station, StationDb
from citibike.entities.station_status import StationStatus

station_status_list = []
station_information = []

# conn = sqlite3.connect('example.db')

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
resp = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')
data = resp.json()['data']['stations']
ebike_available = 0

for datum in data:
    instance = StationStatus()
    for key, value in datum.items():
        if hasattr(instance, key):
            setattr(instance, key, value)
    station_status_list.append(instance)

for status in station_status_list:
    if status.num_ebikes_available > 0:
        stn = StationDb().get_station_by_id(status.station_id)
        # print("{region} {station}: {ebike} ebikes".format(region = stn.region, station=stn.name, ebike=status.num_ebikes_available))
        print("{station}: {ebike} ebikes".format(station=stn.name, ebike=status.num_ebikes_available))
        ebike_available += status.num_ebikes_available

print("{} ebikes available citiwide".format(ebike_available))

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



print(resp.content)