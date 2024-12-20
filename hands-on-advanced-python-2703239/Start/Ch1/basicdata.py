# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
# print(len(weatherdata))

# TODO: What was the coldest day in the data set?
# pprint.pp(weatherdata[0])

# TODO: How many days had snowfall?
#empty dict
years= {}

for d in weatherdata:
    key = d['date'][0:4]
    if key in years:
        years [key] += 1
    else:
        years[key] = 1

pprint.pp(years, width=5)
