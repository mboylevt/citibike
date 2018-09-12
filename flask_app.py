from flask import Flask, render_template

from citibike.util import distance
from citibike.util import bike_util

app = Flask(__name__, template_folder='citibike/templates')

PAS_LATLONG = (40.7436572, -73.9854901)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ebike_template")
def ebike_template():
    region_map = bike_util.get_ebikes()

    return render_template('ebike.html', region_map=region_map)

@app.route("/ebike")
def ebike():
    region_map = bike_util.get_ebikes()
    retstr = ''
    for region, stations in region_map.items():
        retstr += "<div>{}: {} E-bikes</div>".format(region, len(stations))
        retstr += "\n"
        if stations:
            retstr += '<ul>'
            for station, status in stations:
                dist = distance.get_distance(PAS_LATLONG, (station.lat, station.lon))
                retstr += "<li>{name}: {num} bikes, {dist:.2f}m away</li>".format(name=station.name, num=status.num_ebikes_available,
                                                                       dist=dist)
                retstr += "\n"
            retstr += '</ul>'

    return retstr


@app.route('/regions')
def regions():
    region_status = bike_util.get_region_status()
    retstr = ''
    no_bikes = ''
    bikes = ''
    for name in region_status:
        status = region_status[name]
        if status.num_bikes_available == 0:
            no_bikes += "<div>{}: No Bikes Available!</div>".format(name)
        else:
            bikes += "<div>{}:".format(name)
            bikes += '<ul>'
            bikes += "<li>Bikes Available: {num} </li>".format(num=status.num_bikes_available)
            bikes += "<li>eBikes Available: {num} </li>".format(num=status.num_ebikes_available)
            bikes += "<li>Bikes Disabled: {num} </li>".format(num=status.num_bikes_disabled)
            bikes += "<li>Docks Available: {num} </li>".format(num=status.num_docks_available)
            bikes += "<li>Docks Disabled: {num} </li>".format(num=status.num_docks_disabled)
            bikes += '</ul></div>'

    retstr = bikes + no_bikes
    return retstr

if __name__ == "__main__":
    app.run(host='0.0.0.0')
