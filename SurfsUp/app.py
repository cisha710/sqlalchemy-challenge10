# Import the dependencies.
from datetime import datetime, timedelta
from flask import Flask, jsonify
import numpy as np

#Python SQL toolkit and Object Relational Mapper
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
base = automap_base()

# reflect the tables
base.prepare(autoload_with=engine)

# Save references to each table
measurement = base.classes.measurement
station = base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

# 1. Start at the homepage.
#  List all the available routes.@app.route("/")
@app.route("/")
def welcome():
    return (
        f"-----****************************************************************-----<br/>"
        f"Climate analysis of Honolulu, Hawaii..Let's plan a vacation!<br/>"
        f"-----****************************************************************-----<br/>"
        f"<br/>"
        f"Available Routes:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"/api/v1.0/:start<br/>" 
        f"<br/>"
        f"/api/v1.0/:start/:end<br/>"
        f"<br/>"
        f"-----****************************************************************-----"
    )

# 2./api/v1.0/precipitation
# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def prec_data():
  # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Calculate the date one year ago from the last date in the database
    last_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    last_date = datetime.strptime(last_date.date, '%Y-%m-%d')
    one_year_ago = last_date - timedelta(days=365)

      # Query the precipitation data for the last 12 months
    results = session.query(measurement.date, measurement.prcp).filter(
        measurement.date >= one_year_ago
       # measurement.date <= last_date
        ).all()
    
        # Extract the dates and precipitation values from the query results
    # dates = [result.date for result in results]
    # precipitation = [result.prcp if result.prcp is not None else 0 for result in results]


    # Create a dictionary from the row data and append to a list of all_passengers
         
    #data_dict = {date: prcp for date, prcp in zip(dates, precipitation)}
 
    # Return the JSON representation of the dictionary
    return {d:t for d,t in results}




# 3. /api/v1.0/stations
# Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations_list():
  # Create our session (link) from Python to the DB
    session = Session(engine)
    
      # Query the stations list data 
    results = session.query(station.station, station.name).all()
    
       
 
    # Return the JSON representation of the dictionary
    return {id:loc for id,loc in results}




# 4./api/v1.0/tobs
# Query the dates and temperature observations of the most-active station for the previous year of data.
# Return a JSON list of temperature observations for the previous year.
@app.route("/api/v1.0/tobs")
def tobs_data():
    session = Session(engine)
    
      # Query to find most active station
    results = session.query(measurement.date, measurement.tobs).filter(
        (measurement.date >= "2016-08-23")&(measurement.station=="USC00519281")
        ).all()
    
 
    # Return the JSON representation of the dictionary
    return {date:tobo for date,tobo in results}


# 5./api/v1.0/<start> and /api/v1.0/<start>/<end>
# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
@app.route("/api/v1.0/<start_date>")
@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end(start_date, end_date="2017-08-23"):
    session = Session(engine)

    temp_stats = session.query(func.min(measurement.tobs), 
                        func.max(measurement.tobs),
                        func.avg(measurement.tobs)).filter((measurement.date>=start_date)&(measurement.date<=end_date)).first()

    print(temp_stats)

    return {'Lowest Temp':temp_stats[0],'Highest Temp':temp_stats[1],'Avg Temp':temp_stats[2]}
