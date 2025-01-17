import json
import statistics

# Open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# Select the days from the summer months from all the years
summers = ["-06-", "-07-", "-08-"]
summer_months = [d for d in weatherdata if any(month in d['date'] for month in summers)]
print(f"Data for {len(summer_months)} summer days")

# Calculate the mean for both min and max temperatures
max_temps = [day['tmax'] for day in summer_months]
min_temps = [day['tmin'] for day in summer_months]
print(max_mean := statistics.mean(max_temps))
print(min_mean := statistics.mean(min_temps))

# Calculate the median values for min and max temperatures
print(max_median := statistics.median(max_temps))
print(min_median := statistics.median(min_temps))

# Calculate the standard deviation for min and max temperatures
max_stdev = statistics.stdev(max_temps)
min_stdev = statistics.stdev(min_temps)
print(f"Max temperature standard deviation: {max_stdev}")
print(f"Min temperature standard deviation: {min_stdev}")

# Calculate the upper and lower outlier thresholds
upper_outlier = max_mean + 2 * max_stdev
lower_outlier = min_mean - 2 * min_stdev
print(f"Upper outlier threshold: {upper_outlier}")
print(f"Lower outlier threshold: {lower_outlier}")

# Use the standard deviation function to find outlier temperatures
max_outliers = [temp for temp in max_temps if temp >= upper_outlier]
min_outliers = [temp for temp in min_temps if temp <= lower_outlier]

print(f"Max temperature outliers: {max_outliers}")
print(f"Min temperature outliers: {min_outliers}")
