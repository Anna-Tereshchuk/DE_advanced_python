# Example file for Advanced Python: Hands On by Joe Marini
# Arrange data into groups

import json
from collections import defaultdict
import pprint
from itertools import groupby

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# get all the measurements for a particular year
year = [day for day in weatherdata if "2022" in day['date']]

# create manual grouping of days that had a certain level of precipitation
year.sort(key=lambda d: d['prcp'])
datagroup = defaultdict(list)
for d in year:
    datagroup[d['prcp']].append(d['date'])
print(f"{len(datagroup)} total precipitation groups")
pprint.pprint(datagroup)

# Use groupby to get the days of a given year by how much precipitation happened
grouped = groupby(year, key=lambda x: x['prcp'])

# Create a dictionary from the groupby result
grouped_items = {key: list(group) for key, group in grouped}

# How many groups do we have? Now we can use len() on the dictionary
print(f"\n{len(grouped_items)} total precipitation groups using groupby")

# We can iterate over the dictionary to list each group
for precip, data in grouped_items.items():
    print(f"\nPrecipitation: {precip}")
    print(f"Number of days: {len(data)}")
    days = list(map(lambda x: x['date'], data))
    print(f"Days: {days}")
