# sqlalchemy-challenge

This assignment two steps and two bonus analyses that centered around the climate in Hawaii. The steps consisted of (1) Climate Analysis and Exploration, which included a Precipitation Analysis and Station Analysis, and (2) Climate App, which included Routes. On the other hand, the bonus analyses included Temperature Analysis I & II, with the latter including Daily Rainfall Average and Daily Temperature Normals. The information below is a list of tasks that I completed for each respective component.

## Step 1

### Climate Analysis and Exploration

### *Precipitation Analysis*

* Found the most recent date in the data set
* Used date to retrieve the last 12 months of precipitation data by querying the 12 preceding months
* Selected only the `date` and `prcp` values
* Loaded the query results into a Pandas DataFrame and set the index to the date column
* Sorted the DataFrame values by `date`
* Plotted the results using the DataFrame `plot` method *(Please see the graph below)*
* Used Pandas to print the summary statistics for the precipitation data

![image](https://user-images.githubusercontent.com/95979913/158743177-33e0b793-54a0-4403-975c-de48b68a12a0.png)

### *Station Analysis*

* Designed a query to calculate the total number of stations in the dataset
* Designed a query to find the most active stations
* Listed the stations and observation counts in descending order
* Determined which station id has the highest number of observations
* Used the most active station id, calculate the lowest, highest, and average temperature
* Designed a query to retrieve the last 12 months of temperature observation data (TOBS)
* Filtered by the station with the highest number of observations
* Queried the last 12 months of temperature observation data for this station
* Plotted the results as a histogram with `bins=12` *(Please see the graph below)*

![image](https://user-images.githubusercontent.com/95979913/158742943-deeabad0-c843-4426-a9cf-0e056c29fbb4.png)

## Step 2 

### *Climate App*

* Designed a Flask API based on the queries that you have just developed
* Used Flask to create routes *(Please see app.py for more information)*

## Bonus Analyses

### *Temperature Analysis I*

* Use Pandas to determine if there a difference between the temperature in June and December
* Converted the date column format from string to datetime.
* Set the date column as the DataFrame index
* Dropped the date column
* Identified the average temperature in June and December at all stations across all available years in the dataset. 
* Used the t-test to determine whether the difference in the means, if any, is statistically significant. 

### *Temperature Analysis II*

* Used historical data in the dataset to observe previous temperatures
* Used the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from a previous year
* Plotted the min, avg, and max temperature from your previous query as a bar chart
* Used "Trip Avg Temp" as the title
* Used the average temperature as the bar height (y value)
* Used the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR) *(Please see the graph below)*

![image](https://user-images.githubusercontent.com/95979913/158743012-6c57b8c2-72b2-44bb-a96a-37d3ea0c4ab0.png)

### *Daily Rainfall Average*

* Calculated the rainfall per weather station using the previous year's matching dates
* Sorted this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation.

### *Daily Temperature Normals*

* Calculated the daily normals for the duration of your trip, which are the averages for the min, avg, and max temperatures. 
* Set the start and end date of the trip.
* Used the date to create a range of dates.
* Stripped off the year and save a list of strings in the format `%m-%d`.
* Used the `daily_normals` function to calculate the normals for each date string and append the results to a list called `normals`.
* Loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date.
* Used Pandas to plot an area plot (`stacked=False`) for the daily normal *(Please see the graph below)*

![image](https://user-images.githubusercontent.com/95979913/158743082-0cfcb1a6-b1d4-4e58-867e-1a4fbb775d64.png)
