CREATE TABLE IF NOT EXISTS station (
 station_id integer UNIQUE PRIMARY KEY,
 name varchar(255) NOT NULL,
 short_name varchar NOT NULL,
 lat float NOT NULL,
 lon float NOT NULL,
 region_id int NOT NULL,
 rental_methods integer NOT NULL,
 capacity integer NOT NULL,
 rental_url varchar NOT NULL,
 eightd_has_key_dispenser boolean NOT NULL,
 eightd_station_services VARCHAR NOT NULL,
 has_kiosk boolean NOT NULL,
 create_time datetime NOT NULL
);

CREATE TABLE IF NOT EXISTS station_status (
 station_status_id integer PRIMARY KEY AUTOINCREMENT,
 station_id integer NOT NULL,
 num_bikes_available integer NOT NULL,
 num_ebikes_available integer NOT NULL,
 num_bikes_disabled integer NOT NULL,
 num_docks_available integer NOT NULL,
 num_docks_disabled integer NOT NULL,
 is_installed integer NOT NULL,
 is_renting integer NOT NULL,
 is_returning integer NOT NULL,
 last_reported integer NOT NULL,
 eightd_has_available_keys boolean NOT NULL,
 eightd_active_station_services VARCHAR NOT NULL,
 create_time DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS region (
  region_id INTEGER PRIMARY KEY NOT NULL,
  name VARCHAR NOT NULL
)