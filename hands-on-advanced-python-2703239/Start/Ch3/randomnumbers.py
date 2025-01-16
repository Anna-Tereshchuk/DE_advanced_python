# Example file for Advanced Python: Hands On by Joe Marini

import json
import pprint
import random

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the random module can be used to generate random values
print(random.random())  # Генерація випадкового числа з плаваючою точкою між 0 і 1

# choose a random number in a range including both points
print(random.randint(10, 20))  # Включає обидва кінцеві значення

# choose a random number in a range excluding end point
print(random.randrange(10, 20))  # Виключає кінцеве значення

# build a list of the summer days in 2019
def is_summer_day(d):
    summer_months = ["2019-07-", "2019-08-"]
    if any([m in d['date'] for m in summer_months]):
        return True
    return False
summer_2019 = list(filter(is_summer_day, weatherdata))

# choose 5 random days from that summer
random.seed(10)  # Встановлення значення seed для контролю випадкових чисел
random_days = random.sample(summer_2019, 5)

# what was the windiest of those 5 days?
windiest_day = max(random_days, key=lambda day: day.get('wind_speed', day.get('awnd', 0)))

# Виведення результату
pprint.pprint(random_days)
print("Найвітряніший день:", windiest_day)

