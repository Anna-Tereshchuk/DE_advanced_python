# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
# print(len(weatherdata))
warmday = max(weatherdata, key=lambda x: x['tmax'])
print(f"The warmest day was {warmday['date']} at {warmday['tmax']} degrees")
# TODO: What was the coldest day in the data set?
coldday = min(weatherdata, key=lambda x: x['tmin'])
print(f"The coldest day was {warmday['date']} at {warmday['tmin']} degrees")
# pprint.pp(weatherdata[0])

# TODO: How many days had snowfall?
#empty dict
snowdays =[day for day in weatherdata if day ['snow']>0]
print(f"Snow fell on {len(snowdays)}days")
pprint.pp(snowdays)

years= {}

for d in weatherdata:
    key = d['date'][0:4]
    if key in years:
        years [key] += 1
    else:
        years[key] = 1

pprint.pp(years, width=5)
