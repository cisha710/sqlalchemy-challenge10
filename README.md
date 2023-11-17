# SQLAlchamy Challenge
# Honolulu, Hawaii Climate Analysis

## Overview of the analysis
To help with your trip planning so that one can check the climate, one can use this APP to do a climate analysis in that area.


climate_starter.ipynb is updated with the required queries to answer the questions to get the initial analysis.

## API Dynamic Route Analysis: 
1) Designed a Flask API based on the queries that are just developed.
![Screenshot 2023-11-16 at 7 26 46 PM](https://github.com/cisha710/SQLChallenge/assets/143370584/6d4ea2b5-c473-430c-9a88-57af350663a8)

2)A precipitation route to return json with the date as the key and the value as the precipitation.
And it only returns the jsonified precipitation data for the last year in the database.
![Screenshot 2023-11-16 at 8 52 00 PM](https://github.com/cisha710/SQLChallenge/assets/143370584/5956aafd-b22e-4322-93e9-dc899778363a)


3) A stations route returns jsonified data of all of the stations in the database.
![Screenshot 2023-11-16 at 8 52 47 PM](https://github.com/cisha710/SQLChallenge/assets/143370584/115b5afd-41a4-4931-8f40-4979a67e1509)

4) A tobs route /api/v1.0/tobs returns jsonified data for the most active station (USC00519281). It only returns the jsonified data for the last year of data
![Screenshot 2023-11-16 at 8 55 33 PM](https://github.com/cisha710/SQLChallenge/assets/143370584/c47793d2-6576-4cab-8345-3825bd8e45a8)


6) A start route that accepts the start date as a parameter from the URL and it returns the min, max, and average temperatures calculated from the given start date to the end of the dataset.
![Screenshot 2023-11-16 at 7 16 00 PM](https://github.com/cisha710/SQLChallenge/assets/143370584/e80c70ab-c957-4584-8f29-2ecac70a977e)

7) A start/end route that accepts the start and end dates as parameters from the URLto return the min, max, and average temperatures calculated from the given start date to the given end date.
![Screenshot 2023-11-16 at 7 16 29 PM](https://github.com/cisha710/SQLChallenge/assets/143370584/f2c90c96-dc07-4b08-bee4-bb97570344d9)


