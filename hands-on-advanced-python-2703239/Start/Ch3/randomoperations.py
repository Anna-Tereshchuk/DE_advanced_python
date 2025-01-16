import json
import random
import pprint

# Open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# Get the first 30 days in the dataset
month_data = weatherdata[0:30]

# The shuffle() function will randomly shuffle a list in-place
print("Before shuffling:")
pprint.pprint(month_data[:3])
random.shuffle(month_data)
print("After shuffling:")
pprint.pprint(month_data[:3])

# Use choice() and choices() to get random items, but beware that
# these functions can produce duplicate results
rnd_day = random.choice(month_data)
print("Random day:")
pprint.pprint(rnd_day)

rnd_days = random.choices(month_data, k=3)
print("Random days:")
pprint.pprint(rnd_days)

# Use sample() to get unique random items
unique_days = random.sample(month_data, 3)
print("Unique random days:")
pprint.pprint(unique_days)






# TODO: the sample() function will choose random items with no duplicates
