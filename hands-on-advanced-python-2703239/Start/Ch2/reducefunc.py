import json
from functools import reduce

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: how much snowfall is in the entire dataset?
total_snowfall = reduce(
    lambda acc, el: acc + el['snow'],
    weatherdata,
    0
)
print(f"Total snowfall: {total_snowfall} inches")

# TODO: how much total precipitation is in the entire dataset?
total_precip = reduce(
    lambda acc, el: acc + el['snow'] + el['prcp'],
    weatherdata,
    0
)
print(f"Total precipitation: {total_precip} inches")

# TODO: What was the warmest day in which it snowed? Need to find highest 'tmax' for all
# days where 'snow' > 0
def warm_snow_day(acc, elem):
    if elem['snow'] > 0 and (acc is None or elem['tmax'] > acc['tmax']):
        return elem
    return acc

# define a "zero" value start date for the reduce function to start with
start_val = None

# TODO: reduce the data set to the warmest snow day
warmest_snow_day = reduce(warm_snow_day, weatherdata, start_val)

# Print the result
if warmest_snow_day:
    print(f"The warmest day on which it snowed was {warmest_snow_day['date']} with a max temperature of {warmest_snow_day['tmax']} and snowfall of {warmest_snow_day['snow']}")
else:
    print("No day with snowfall found in the dataset.")

