from citibike.entities.citibike_db import CitibikeDb


class Station():
    def __init__(self, station_id=None, name=None, short_name=None, lat=None, lon=None, rental_methods=None,
                 capacity=None, rental_url=None, eightd_has_key_dispenser=None, eightd_station_services=None,
                 has_kiosk=None,
                 ):
        self.station_id = station_id
        self.name = name
        self.short_name = short_name
        self.lat = lat
        self.lon = lon
        self.rental_methods = rental_methods
        self.capacity = capacity
        self.rental_url = rental_url
        self.eightd_has_key_dispenser = eightd_has_key_dispenser
        self.eightd_station_services = eightd_station_services
        self.has_kiosk = has_kiosk


class StationDb(CitibikeDb):
    def __init__(self):
        super(CitibikeDb, self).__init__()

    def insert_station(self):
        pass