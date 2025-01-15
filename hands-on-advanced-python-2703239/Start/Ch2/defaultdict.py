import json
import pprint
from collections import defaultdict

# Відкриття файлу з даними про погоду та завантаження їх за допомогою модуля json
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# Підрахунок кількості записів для кожного року за допомогою defaultdict
years = defaultdict(int)
for day in weatherdata:
    year = day['date'][:4]
    years[year] += 1

print("Number of data points for each year:")
pprint.pprint(dict(years))

# Використання defaultdict зі списками для зберігання днів за місяцями
years_months = defaultdict(list)
for day in weatherdata:
    year_month = day['date'][:7]
    years_months[year_month].append(day)

print("\nNumber of keys (year-month) in the dictionary:")
print(len(years_months))

# Функції для визначення найтеплішого та найхолоднішого дня місяця
def warmest_day(month):
    wd = max(month, key=lambda d: d['tmax'])
    return (wd['date'], wd['tmax'])

def coldest_day(month):
    cd = min(month, key=lambda d: d['tmin'])
    return (cd['date'], cd['tmin'])

# Обхід ключів словника та визначення найтеплішого та найхолоднішого дня кожного місяця
for year_month, days in years_months.items():
    warmest = warmest_day(days)
    coldest = coldest_day(days)
    print(f"\nThe warmest day in {year_month} was {warmest[0]} with a max temperature of {warmest[1]}")
    print(f"The coldest day in {year_month} was {coldest[0]} with a min temperature of {coldest[1]}")
