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

#########################################
# configure longitude and latitude here #
#########################################
lat = 1.2804
lon = 103.8408
print('Durian') # location name
# lat = 3.8617
# lon = 11.5202
# print('Yaounde')
# lat = 40.7722
# lon = -73.9730
# print('Central Park Manhattan')
# lat = 90
# lon = 0
# print('North Pole')
# lat = 25.7617
# lon = -80.1918
# print('Miami')


# gather all the info of a year in a given location
days = []
for i in range(365):
    day = datetime.strptime(spring_equinox, "%Y/%m/%d") + timedelta(days=i)
    day_results = getSunInfoSingle(lat, lon, day)
    print(day_results)
    days.append(day_results)
    # [day, sunrise_time, midday, sunset_time, total_hours] = results format

# create plotable lists of data
X_axis_days = list(range(365))
Y_axis_sun_hours = [res[4].total_seconds() / 3600 for res in days]
Y_axis_sunrise = [int(res[1].replace(':','')) for res in days]
Y_axis_midday = [int(res[2].replace(':','')) for res in days]
Y_axis_sunset = [int(res[3].replace(':','')) for res in days]

# print longest and shortest day lengths to console
longest_day = 0
shortest_day = 13
for d in Y_axis_sun_hours:
    if d > longest_day:
        longest_day = d
    if d < shortest_day:
        shortest_day = d
print(f'Longest day = {longest_day} hours')
print(f'Shortest day = {shortest_day} hours')


plt.figure(figsize=(10, 5))

#######################
# configure axes here #
#######################
plt.plot(X_axis_days, Y_axis_sun_hours, label='Total Sun Hours')
# plt.plot(X_axis_days, Y_axis_midday, label='True Midday Hour')

#########################
# configure labels here #
#########################
plt.title('Sun Hours Throughout the Year')
plt.xlabel('Day of the Year (Beginning from Spring Equinox)')
plt.ylabel('Total Hours')
# example titles:
# Sun Hours Throughout the Year in NYC (40.7722° N, 73.9730° W)
# Sun Hours Throughout the Year in Singapore (1.2804° N, 103.8408° E)
# Midday Hour Throughout the Year in Miami (25.7617° N, 80.1918° W)

plt.grid(True)
plt.legend()
plt.show()


