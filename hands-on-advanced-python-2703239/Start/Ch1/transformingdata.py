# Example file for Advanced Python: Hands On by Joe Marini
# Transform data from one format to another

import json
import copy
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the map() function is used to transform data from one form to another
# Let's convert the weather data from imperial to metric units
def ToC(f):
    return (f - 32) * 5/9 if f is not None else None

def ToMM(i):
    return i * 25.4 if i is not None else None

def ToKPH(s):
    return s * 1.60934 if s is not None else None

def ToMetric(wd):
    new_wd = copy.copy(wd)
    new_wd['tmin'] = ToC(wd.get('tmin'))
    new_wd['tmax'] = ToC(wd.get('tmax'))
    new_wd['prcp'] = ToMM(wd.get('prcp'))
    new_wd['snow'] = ToMM(wd.get('snow'))
    new_wd['snwd'] = ToMM(wd.get('snwd'))
    new_wd['awnd'] = ToKPH(wd.get('awnd'))
    return new_wd

# Use map() to call ToMetric and convert weatherdata to metric
metric_weatherdata = list(map(ToMetric, weatherdata))

# use the map() function to convert objects to tuples
# in this case, create tuples with a date and the average of tmin and tmax
Avg_Temp = lambda t1, t2: (t1 + t2) / 2.0 if t1 is not None and t2 is not None else None
date_avg_temp = list(map(lambda wd: (wd['date'], Avg_Temp(wd['tmin'], wd['tmax'])), metric_weatherdata))

# Pretty print the results
pprint.pprint(metric_weatherdata)
pprint.pprint(date_avg_temp)

