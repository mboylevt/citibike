from math import sin, cos, sqrt, atan2, radians


def get_distance(origin, station, miles=True):
    R = 6373.0 # approximate radius of earth in km

    lat1 = radians(origin[0])
    lon1 = radians(origin[1])
    lat2 = radians(station[0])
    lon2 = radians(station[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    dist = R * c
    if miles:
        return dist*.621371
    return dist