import requests

from citibike.entities.station_status import StationStatus

station_status_list = []


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
"url": "https://gbfs.citibikenyc.com/gbfs/en/system_regions.json"
},
{
"name": "station_information",
"url": "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"
}
]
"""
resp = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')
data = resp.json()['data']['stations']


for datum in data:
    instance = StationStatus()
    for key, value in datum.items():
        if hasattr(instance, key):
            setattr(instance, key, value)
    station_status_list.append(instance)
    print(instance)

print(resp.content)