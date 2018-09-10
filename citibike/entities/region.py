import time

import datetime

from citibike.entities.citibike_db import CitibikeDb

REGION_TABLE = 'region'


class Region():
    def __init__(self, region_id=None, name=None):
        self.region_id = region_id
        self.name = name


class RegionDb(CitibikeDb):
    def __init__(self):
        super(RegionDb, self).__init__()

    def insert_region(self, region):
        sql = """INSERT INTO {table} (region_id, name) VALUES ({region_id}, "{name}")""".format(
            table=REGION_TABLE,
            region_id=region.region_id,
            name=region.name,
        )

        self.insert(sql)

    def get_region_by_id(self, region_id):
        """

        :param station_id: Id of station to retrieve
        :type station_id: int
        :return:
        """
        sql = """SELECT * from {table} WHERE region_id = {region_id}""".format(
            table=REGION_TABLE,
            station_id=region_id
        )

        return self.get_single_instance(sql, Region)


