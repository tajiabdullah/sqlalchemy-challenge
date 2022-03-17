from flask import Flask, jsonify
import numpy as np
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime, timedelta
from itertools import chain

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Data/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Please see the available API routes below:<br/><br/>"
        f"1. Precipitation: /api/v1.0/precipitation<br/><br/>"
        f"2. List of Stations: /api/v1.0/stations<br/><br/>"
        f"3. Temperatures from 08/24/2016 to 08/23/2017: /api/v1.0/tobs<br/><br/>"
        f"4. Temperatures from a specific start date (YYYY-MM-DD): /api/v1.0/yyyy-mm-dd<br/>"
        f"(Please note that the start should be formatted as 'YYYY-MM-DD')<br/><br/>"
        f"5. Temperatures from a specific start date to a specific end date (YYYY-MM-DD): /api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br/>"
        f"(Please note that the start and end date should be formatted as 'YYYY-MM-DD')"
    )

#################################################

@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    sel = [Measurement.date,Measurement.prcp]
    queryresult = session.query(*sel).all()
    session.close()

    precipitation = []
    for date, prcp in queryresult:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        precipitation.append(prcp_dict)

    return jsonify(precipitation)

#################################################

@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    sel = [Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation]
    queryresult = session.query(*sel).all()
    session.close()

    stations = []
    for station,name,lat,lon,el in queryresult:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Latitude"] = lat
        station_dict["Longitude"] = lon
        station_dict["Elevation"] = el
        stations.append(station_dict)

    return jsonify(stations)

#################################################

@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    lateststr = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    latestdate = dt.datetime.strptime(lateststr, '%Y-%m-%d')
    querydate = dt.date(latestdate.year -1, latestdate.month, latestdate.day)
    sel = [Measurement.date,Measurement.tobs]
    queryresult = session.query(*sel).filter(Measurement.date >= querydate).all()
    session.close()

    tobsall = []
    for date, tobs in queryresult:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Temperature"] = tobs
        tobsall.append(tobs_dict)

    return jsonify(tobsall)

#################################################

@app.route('/api/v1.0/<start>')
def get_temperature_start(start):
    session = Session(engine)
    queryresult = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    session.close()

    tobsall = []
    for min,avg,max in queryresult:
        tobs_dict = {}
        tobs_dict["Minimum Temperature"] = min
        tobs_dict["Average Temperature"] = avg
        tobs_dict["Maximum Temperature"] = max
        tobsall.append(tobs_dict)

    return jsonify(tobsall)

#################################################

@app.route('/api/v1.0/<start>/<stop>')
def get_temperature_start_stop(start,stop):
    session = Session(engine)
    queryresult = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= stop).all()
    session.close()

    tobsall = []
    for min,avg,max in queryresult:
        tobs_dict = {}
        tobs_dict["Minimum Temperature"] = min
        tobs_dict["Average Temperature"] = avg
        tobs_dict["Maximum Temperature"] = max
        tobsall.append(tobs_dict)

    return jsonify(tobsall)

#################################################

if __name__ == '__main__':
    app.run(debug=True)