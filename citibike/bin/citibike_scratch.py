import requests
import sqlite3


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



# print(resp.content)