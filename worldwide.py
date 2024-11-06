from horasdeluz import getSunInfoSingle
from datetime import datetime, timedelta, date
import matplotlib.pyplot as plt


# static latitude eg. equator, 23.26, 66.34
#     # observations:
#     # repeating triplets pattern in sunrise when changing longitude
#     # equator = constant daylight 12 hours regardless of time of year give or take a min or two
#     # tropic of cancer = ~10h42m(shortest day) to ~13h35m(longest day)
#     # arctic circle = ~(shortest day) to ~(longest day)


# # static longitude eg. Miami, prime meridian, Singapore
#     # observations:
#     # no change whatsoever as longitude is changed
#     # around 12 hours all accross the board at both equinoxes
#     # after spring equinox north days get long and south days get short
#     # after fall equinox north days get short and south days get long

today = date.today().strftime('%Y/%m/%d')

spring_equinox = '2024/03/19' # days back to +12hr after here
ss_mid = '2024/05/05'
summer_solstice = '2024/06/20' # longest day
sf_mid = '2024/08/05'
fall_equinox = '2024/09/22' # days get are -12hrs after here
fw_mid = '2024/11/07'
winter_solstice = '2024/12/21' # shortest day

unique_days = [today, spring_equinox, ss_mid, summer_solstice, sf_mid, fall_equinox, fw_mid, winter_solstice]

lat = 3.8617
lon = 11.5202
print('Yaounde')

# gather all the info of a year in a given location
days = []
for i in range(365):
    day = datetime.strptime(spring_equinox, "%Y/%m/%d") + timedelta(days=i)
    day_results = getSunInfoSingle(lat, lon, day)
    day_results.insert(0, day)
    days.append(day_results)
    # [day, latitude, longitude, sunrise, sunset, day length] = results format

X_axis_days = list(range(365))
Y_axis_sun_hours = [res[5].total_seconds() / 3600 for res in days]
Y_axis_sunrise = [int(res[3].replace(':','')) for res in days]
Y_axis_sunset = [int(res[4].replace(':','')) for res in days]

plt.figure(figsize=(10, 5))
plt.plot(X_axis_days, Y_axis_sun_hours, label='Sun Hours')
plt.title('Sun Hours Throughout the Year')
plt.xlabel('Day of the Year Starting on Summer Solstice')
plt.ylabel('Number of Hours')
plt.grid(True)
plt.legend()
plt.show()


