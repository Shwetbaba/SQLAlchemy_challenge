#Importing libraries
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData
from sqlalchemy.pool import StaticPool
from flask import Flask, jsonify
import datetime as dt
import re
from operator import itemgetter



app = Flask(__name__)
@app.route("/")
def welcome():
    return (
    
        f"🕉️🙏🏼Welcome to the customized climate API application🙏🏼🕉️<br/>"
        f"<hr><hr/>"
        f"<hr><hr/>"
        f"Please copy the following links at the end of flask server http address '***.*.*.*.*:****' one by one to view specific parameters::<br/>"  
        f"<br><br/>"
        f"/api/aboutme<br/>"
        f"/api/precipitation<br/>"
        f"/api/stations<br/>"
        f"/api/tobs<br/>")



@app.route("/api/aboutme")
def about():
    name = "Shwet 'Sunny' Bhatt"
    location = "San Antonio, TX"

    return f"My name is {name}, I'm from {location}. I am enterprising to be a Sr. Data Scientist."

#Create engine and make connection
engine = create_engine("sqlite:///Resources/hawaii.sqlite",
    connect_args={'check_same_thread':False},
    poolclass=StaticPool)



# Create our session engine from Python and reflect existing database in a new model
session = Session(engine)
Base = automap_base()
# Reflecting tables
Base.prepare(engine, reflect=True)
# Saving reference for each table
Measurement = Base.classes.measurement
Station = Base.classes.station



# Define function route
@app.route("/api/precipitation")
def precipitation():
    # Calculate the date 1 year ago from the last data point in the database
    last_data_point_query = session.query(func.max(Measurement.date))
    for record in last_data_point_query:
        last_date = record 
        print(last_date)
    #Convert to string
    lastdatestring = str(last_date)
    print(lastdatestring)
    match = re.search('\d{4}-\d{2}-\d{2}', lastdatestring)
    last_date = dt.datetime.strptime(match.group(), '%Y-%m-%d').date()
    print(last_date)
    previous_years = last_date - dt.timedelta(days=365)
    print(previous_years)



    #date_input = input("Enter a date between: {previous_years} and {last_date}")
    # Perform a query to retrieve the data and precipitation scores
    sel = [Measurement.date,Measurement.prcp]
    data = session.query(*sel).filter(Measurement.date >= previous_years).all()



    # Return the JSON representation of your dictionary.
    # Create a dictionary from the row data and append to a list of all_passengers
    precipitation_data = []
    for row in data:
        precipitation_dict = {}
        precipitation_dict["date"] = row.date
        precipitation_dict["prcp"] = row.prcp
        precipitation_data.append(precipitation_dict)
    
    prcp_data = sorted(precipitation_data, key=itemgetter('date')) 

    return jsonify(prcp_data)



# Define function route
@app.route("/api/stations")
def stations():

#Returning with JSON list of stations from the dataset
# Designing query to show total stations available in dataset
    station_count_query = session.query(Station.station,Station.name).all()
    station_list = []
    for row in station_count_query:
        station_dict = {}
        station_dict['station'] = row.station
        station_dict['name'] = row.name
        station_list.append(station_dict)
    return jsonify(station_list)



# Define function route
@app.route("/api/tobs")
def tobs():



# query for the dates and temperature observations from a year from the last data point.
# Return a JSON list of Temperature Observations (tobs) for the previous year.
    last_data_point_query = session.query(func.max(Measurement.date))
    for record in last_data_point_query:
        last_date = record 
        print(last_date)
    lastdatestring = str(last_date)
    match = re.search('\d{4}-\d{2}-\d{2}', lastdatestring)
    last_date = dt.datetime.strptime(match.group(), '%Y-%m-%d').date()
    previous_years = last_date - dt.timedelta(days=365)
    station_measurement_query = session.query(Measurement.station,func.count(Measurement.date)).group_by(Measurement.station).\
                                              order_by(func.count(Measurement.date).desc())
    result = [r.station for r in station_measurement_query]
    mostactivestation = result[0]
    sel_tobs = [Measurement.station,Measurement.date,Measurement.tobs]
    query_tobs = session.query(*sel_tobs).filter(Measurement.date >= previous_years).filter(Measurement.station == mostactivestation)
    data_tobs = query_tobs.all()
    tobs_list = []
    for row in data_tobs:
        tobs_dict = {}
        tobs_dict['station'] = row.station
        tobs_dict['date'] = row.date
        tobs_dict['tobs'] = row.tobs
        tobs_list.append(tobs_dict)
    return jsonify(tobs_list)



#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
@app.route("/api/<start>") 
def calc_temps(start):
    start = dt.datetime.strptime(start, "%Y-%m-%d").date()



#For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
    start_date_query = session.query(func.min(Measurement.tobs).label('tmin'), func.avg(Measurement.tobs).label('tavg'), func.max(Measurement.tobs).label('tmax')).\
                        filter(Measurement.date >= start).all()
    st_date_list = []
    for row in start_date_query:
        calc_temp_s = {}
        calc_temp_s['tmin'] = row.tmin
        calc_temp_s['tavg'] = row.tavg
        calc_temp_s['tmax'] = row.tmax
        st_date_list.append(calc_temp_s)
    return jsonify(st_date_list)


@app.route("/api/<start>/<end>")
def calc_temps2(start, end):
    start = dt.datetime.strptime(start, "%Y-%m-%d").date()
    end = dt.datetime.strptime(end, "%Y-%m-%d").date()
    st_end_date_query =  session.query(func.min(Measurement.tobs).label('tmin'), func.avg(Measurement.tobs).label('tavg'), func.max(Measurement.tobs).label('tmax')).\
                         filter(Measurement.date >= start).filter(Measurement.date <= end).all()



#For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
    st_end_date_list = []
    for row in st_end_date_query:
        calc_temp_s_e = {}
        calc_temp_s_e['tmin'] = row.tmin
        calc_temp_s_e['tavg'] = row.tavg
        calc_temp_s_e['tmax'] = row.tmax
        st_end_date_list.append(calc_temp_s_e)
    return jsonify(st_end_date_list)

if __name__ == "__main__":
    app.run(debug=True)






















































































































































































































































































































##Reference : https://github.com/kunal-soni/SQL_Alchemy_Flask_SurfsUp_Climate_Analysis