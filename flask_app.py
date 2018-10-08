from flask import Flask, render_template, send_from_directory

from citibike.util import distance
from citibike.util import bike_util

app = Flask(__name__, template_folder='citibike/templates')

PAS_LATLONG = (40.7436572, -73.9854901)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/static/css/<path:path>')
def send_static_css(path):
    return send_from_directory('citibike/static/css', path)

@app.route('/static/js/<path:path>')
def send_static_js(path):
    return send_from_directory('citibike/static/js', path)

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

@app.route("/ebike")
def ebike_template():
    region_map = bike_util.get_ebikes()
    region_status = {}

    for region, stations in region_map.items():
        bike_count = 0
        region_status[region] = []
        if stations:
            for station, status in stations:
                dist = distance.get_distance(PAS_LATLONG, (station.lat, station.lon))
                region_status[region].append((station.name, status.num_ebikes_available, dist, region))
                bike_count += status.num_ebikes_available
            region_status[region] = [bike_count] + region_status[region]
        else:
            region_status[region].append(0)


    return render_template('ebike.html', region_status=region_status)

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
