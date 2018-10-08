import time

import datetime

from citibike.entities.citibike_db import CitibikeDb

STATION_TABLE = 'station'

class Station():
    def __init__(self, station_id=None, name=None, short_name=None, lat=None, long=None, region_id = None,
                 rental_methods=None, capacity=None, rental_url=None, eightd_has_key_dispenser=None,
                 eightd_station_services=None,has_kiosk=None, create_time=None
                 ):
        self.station_id = station_id
        self.name = name
        self.short_name = short_name
        self.lat = lat
        self.lon = long
        self.region_id = region_id
        self.rental_methods = rental_methods
        self.capacity = capacity
        self.rental_url = rental_url
        self.eightd_has_key_dispenser = eightd_has_key_dispenser
        self.eightd_station_services = eightd_station_services
        self.has_kiosk = has_kiosk
        self.create_time = create_time


class StationDb(CitibikeDb):
    def __init__(self):
        super(StationDb, self).__init__()

    def insert_station(self, station):
        sql = """INSERT INTO {table} (station_id, name, short_name, lat, lon, region_id, rental_methods, capacity, rental_url, 
              eightd_has_key_dispenser, eightd_station_services, has_kiosk, create_time) VALUES ({station_id}, "{name}", "{short_name}", 
              {lat}, {lon}, {region_id}, "{rental_methods}", {capacity}, "{rental_url}", {eightd_has_key_dispenser}, 
              "{eightd_station_services}",{has_kiosk},"{create_time}")
                """.format(
            table=STATION_TABLE,
            station_id=station.station_id,
            name=station.name,
            short_name=station.short_name,
            lat=station.lat,
            lon=station.lon,
            region_id=station.region_id if station.region_id else 999,
            rental_methods=station.rental_methods,
            capacity=station.capacity,
            rental_url=station.rental_url,
            eightd_has_key_dispenser=int(station.eightd_has_key_dispenser),
            eightd_station_services=station.eightd_station_services,
            has_kiosk=int(station.has_kiosk),
            create_time=datetime.datetime.now()
        )

        self.insert(sql)

    def get_station_by_id(self, station_id):
        """

        :param station_id: Id of station to retrieve
        :type station_id: int
        :return:
        :rtype: Station
        """
        sql = """SELECT * from {table} WHERE station_id = {station_id}""".format(
            table=STATION_TABLE,
            station_id=station_id
        )

        return self.get_single_instance(sql, Station)


