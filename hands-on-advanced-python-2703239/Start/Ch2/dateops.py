# Example file for Advanced Python: Hands On by Joe Marini
# Working with date values

from datetime import date, timedelta
import json



# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)


# TODO: The datetime module converts strings into dates fairly easily
date_str = weatherdata[0]['date']
date_obj = date.fromisoformat(date_str)
print(f"Converted date: {date_obj}")


# TODO: Date objects give us information such as day of week (0=Monday, 6=Sunday)
date_str = weatherdata[0]['date']
date_obj = date.fromisoformat(date_str)
print(f"Converted date: {date_obj}")
print(f"Day of the week: {date_obj.weekday()}")  # 0=Monday, 6=Sunday


# TODO: what was the warmest weekend day in the dataset?
def is_weekend_day(day_str):
    day = date.fromisoformat(day_str)
    return day.weekday() == 5 or day.weekday() == 6

weekend_days = list(filter(lambda x: is_weekend_day(x['date']), weatherdata))
warmest_weekend_day = max(weekend_days, key=lambda x: x['tmax'])
print(f"The warmest weekend day was {warmest_weekend_day['date']} with a max temperature of {warmest_weekend_day['tmax']}")



# The timedelta object provides an easy way of performing date math
# find the coldest day of the year and get the average temp for the following week
# coldest_day = min(weatherdata, key=lambda d: d['tmin'])
# convert the date to a Python date
# coldest_date = date.fromisoformat(coldest_day['date'])
# print(f"The coldest day of the year was {str(coldest_date)} ({coldest_day['tmin']})")
coldest_day = min(weatherdata, key=lambda d: d['tmin'])
coldest_date = date.fromisoformat(coldest_day['date'])
print(f"The coldest day of the year was {coldest_date} with a min temperature of {coldest_day['tmin']}")

def calculate_weekly_average(start_date_str):
    start_date = date.fromisoformat(start_date_str)
    total_temp = 0
    count = 0

    for i in range(7):
        next_date = start_date + timedelta(days=i)
        next_date_str = next_date.isoformat()
        for day in weatherdata:
            if day['date'] == next_date_str:
                avg_temp = (day['tmin'] + day['tmax']) / 2
                total_temp += avg_temp
                count += 1
                break

    if count == 0:
        return None
    return total_temp / count

weekly_avg_temp = calculate_weekly_average(coldest_day['date'])
if weekly_avg_temp is not None:
    print(f"The average temperature for the week starting on {coldest_day['date']} was {weekly_avg_temp:.2f} degrees Fahrenheit")
else:
    print(f"No data available for the week starting on {coldest_day['date']}")

# TODO: Look up the next 7 days
coldest_day = min(weatherdata, key=lambda d: d['tmin'])
coldest_date = date.fromisoformat(coldest_day['date'])
print(f"The coldest day of the year was {coldest_date} with a min temperature of {coldest_day['tmin']}")

def calculate_weekly_average(start_date_str):
    start_date = date.fromisoformat(start_date_str)
    total_temp = 0
    count = 0

    for i in range(7):
        next_date = start_date + timedelta(days=i)
        next_date_str = next_date.isoformat()
        for day in weatherdata:
            if day['date'] == next_date_str:
                avg_temp = (day['tmin'] + day['tmax']) / 2
                total_temp += avg_temp
                count += 1
                break

    if count == 0:
        return None
    return total_temp / count

weekly_avg_temp = calculate_weekly_average(coldest_day['date'])
if weekly_avg_temp is not None:
    print(f"The average temperature for the week starting on {coldest_day['date']} was {weekly_avg_temp:.2f} degrees Fahrenheit")
else:
    print(f"No data available for the week starting on {coldest_day['date']}")
