# Example file for Advanced Python: Hands On by Joe Marini
# Filter values out of a data set based on some criteria

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the filter() function gives us a way to remove unwanted data points
# TODO: create a subset of the data for days that had snowfall
snow_days = list(filter(lambda day: day['snow'] > 0.0, weatherdata))
#print(len(weatherdata))
#print(len(snow_days))


# TODO: pretty-print the resulting data set
pprint.pp(snow_days)

# filter can also be used on non-numerical data, like strings
# TODO: create a subset that contains summer days with heavy rain (more than 1 in, about 2.5cm)


def is_summer_rain_day(d):
    summer_months = ["-07-", "-08-"]
    # Check if the date belongs to the summer months and the precipitation is >= 1 inch
    if any(month in d['date'] for month in summer_months) and d['prcp'] >= 1.0:
        return True  # This is a summer rain day
    return False  # Otherwise, it is not

summer_rain_days = list(filter(is_summer_rain_day, weatherdata))
print(len(weatherdata))
print(len(snow_days))
pprint.pp(summer_rain_days)