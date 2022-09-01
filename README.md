# Unit 10 Homework: Surf’s Up

## Before You Begin

1. Create a new repository for this project called `sqlalchemy-challenge`. **Do not add this homework to an existing repository**.

2. Clone the new repository to your computer.

3. Add your Jupyter notebook and `app.py` to this folder. These will be the main scripts to run for analysis.

4. Push the changes to GitHub or GitLab.

![surfs-up.png](Images/surfs-up.png)

## Instructions

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following sections outline the steps you must take to accomplish this task.

### Part 1: Climate Analysis and Exploration

In this section, you’ll use Python and SQLAlchemy to perform basic climate analysis and data exploration of your climate database. Complete the following tasks by using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Use the provided [starter notebook](climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) files to complete your climate analysis and data exploration.

* Use SQLAlchemy’s `create_engine` to connect to your SQLite database.

* Use SQLAlchemy’s `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

* Link Python to the database by creating a SQLAlchemy session.

* **Important:** Don't forget to close out your session at the end of your notebook.

#### Precipitation Analysis

To perform an analysis of precipitation in the area, do the following:

* Find the most recent date in the dataset.

* Using this date, retrieve the previous 12 months of precipitation data by querying the 12 previous months of data. **Note:** Do not pass in the date as a variable to your query.

* Select only the `date` and `prcp` values.

* Load the query results into a Pandas DataFrame, and set the index to the date column.

* Sort the DataFrame values by `date`.

* Plot the results by using the DataFrame `plot` method, as shown in the following image:

  ![precipitation](Images/precipitation.png)

* Use Pandas to print the summary statistics for the precipitation data.

#### Station Analysis

To perform an analysis of stations in the area, do the following:

* Design a query to calculate the total number of stations in the dataset.

* Design a query to find the most active stations (the stations with the most rows).

    * List the stations and observation counts in descending order.

    * Which station id has the highest number of observations?

    * Using the most active station id, calculate the lowest, highest, and average temperatures.

    * **Hint:** You will need to use functions such as `func.min`, `func.max`, `func.avg`, and `func.count` in your queries.

* Design a query to retrieve the previous 12 months of temperature observation data (TOBS).

    * Filter by the station with the highest number of observations.

    * Query the previous 12 months of temperature observation data for this station.

    * Plot the results as a histogram with `bins=12`, as shown in the following image:

    ![station-histogram](Images/station-histogram.png)

* Close out your session.

- - -

### Part 2: Design Your Climate App

Now that you have completed your initial analysis, you’ll design a Flask API based on the queries that you have just developed.

Use Flask to create your routes, as follows:

* `/`

    * Homepage.

    * List all available routes.

* `/api/v1.0/precipitation`

    * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

    * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

    * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`

    * Query the dates and temperature observations of the most active station for the previous year of data.

    * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

    * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.

    * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than or equal to the start date.

    * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates from the start date through the end date (inclusive).

## Hints

* You will need to join the station and measurement tables for some of the queries.

* Use Flask `jsonify` to convert your API data into a valid JSON response object.

### Bonus: Other Recommended Analyses

The following are optional challenge queries that we recommend you attempt, but they are not required for this assignment.

* Use the provided [temp_analysis_bonus_1_starter.ipynb](temp_analysis_bonus_1_starter.ipynb) and [temp_analysis_bonus_2_starter.ipynb](temp_analysis_bonus_2_starter.ipynb) starter notebooks for their respective bonus challenge.

#### Temperature Analysis 1

Conduct an analysis to answer the following question: Hawaii is reputed to enjoy mild weather all year round. Is there a meaningful difference between the temperatures in, for example, June and December?

* Use Pandas to perform the following steps:

    * Convert the date column format from `string` to `datetime`.

    * Set the date column as the DataFrame index.

    * Drop the date column.

* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for the temperature in December.

* Use the t-test to determine whether the difference in means, if any, is statistically significant. Will you use a paired t-test or an unpaired t-test? Why?

#### Temperature Analysis 2

You want to take a trip from August 1 to August 7 of this year, but you are worried that the weather will be less than ideal. Using historical data in the dataset, find out what the temperature has previously been for this timeframe.

**Note:** The starter notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.

Complete the following steps:

* Use the `calc_temps` function to calculate the minimum, average, and maximum temperatures for your trip using the matching dates from a previous year (for example, use "2017-08-01").

* Plot the minimum, average, and maximum temperature from your previous query as a bar chart, as captured in the following steps and image:

    * Use "Trip Avg Temp" as the title.

    * Use the average temperature as the bar height (_y_ value).

    * Use the peak-to-peak (TMAX-TMIN) value as the _y_ error bar (YERR).

    ![temperature](Images/temperature.png)

#### Daily Rainfall Average

Now that you have an idea of the temperature, let’s find out what the rainfall has been. You don't want to visit if it rains the whole time! Complete the following steps:

* Calculate the rainfall per weather station using the previous year's matching dates.

    * Sort this in descending order by precipitation amount, and list the station, name, latitude, longitude, and elevation.

### Daily Temperature Normals

Calculate the daily normals for the duration of your trip. Normals are the averages for the minimum, average, and maximum temperatures.

You are provided with a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Make sure to use all historic TOBS that match that date string.

Complete the following steps:

* Set the start and end date of the trip.

* Use the date to create a range of dates.

* Strip off the year, and save a list of strings in the format `%m-%d`.

* Use the `daily_normals` function to calculate the normals for each date string, and append the results to a list called `normals`.

* Load the list of daily normals into a Pandas DataFrame, and set the index equal to the date.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals, as shown in the following image:

  ![daily-normals](Images/daily-normals.png)

* Close out your session.

## Rubric

[Unit 10 Homework Rubric](https://docs.google.com/document/d/1gT29iMF3avSvJruKpcHY4qovP5QitgXePqtjC6XESI0/edit?usp=sharing)

- - -

## References

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, [https://doi.org/10.1175/JTECH-D-11-00103.1](https://doi.org/10.1175/JTECH-D-11-00103.1)

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
