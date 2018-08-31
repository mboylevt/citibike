class StationStatus:
    def __init__(self, station_id=None, num_bikes_available=None, num_ebikes_available=None, num_bikes_disabled=None, num_docks_available=None,
                 num_docks_disabled=None, is_installed=None, is_renting=None, is_returning=None, last_reported=None, eightd_has_available_keys=None,
                 eightd_active_station_services=None):
        self.station_id = station_id
        self.num_bikes_available = num_bikes_available
        self.num_ebikes_available = num_ebikes_available
        self.num_bikes_disabled = num_bikes_disabled
        self.num_docks_available = num_docks_available
        self.num_docks_disabled = num_docks_disabled
        self.is_installed = is_installed
        self.is_renting = is_renting
        self.is_returning = is_returning
        self.last_reported = last_reported
        self.eightd_has_available_keys = eightd_has_available_keys
        self.eightd_active_station_services = eightd_active_station_services