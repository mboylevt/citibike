from flask import Flask

from citibike.util import distance
from citibike.util.ebike import get_ebikes

app = Flask(__name__)

PAS_LATLONG = (40.7436572, -73.9854901)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ebike")
def ebike():
    region_map = get_ebikes()
    retstr = ''
    for region, stations in region_map.items():
        retstr += "<div>{}: {} bikes</div>".format(region, len(stations))
        retstr += "\n"
        if stations:
            retstr += '<ul>'
            for station, status in stations:
                dist = distance.get_distance(PAS_LATLONG, (station.lat, station.lon))
                retstr += "<li>{name}: {num} bikes, {dist:.2f}m away</li>".format(name=station.name, num=status.num_ebikes_available,
                                                                       dist=dist)
                retstr += "\n"
            retstr += '</ul>'

    print(retstr)
    return retstr

if __name__ == "__main__":
    app.run(host='0.0.0.0')