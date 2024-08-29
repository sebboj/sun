from horasdeluz import getSunInfoSingle
import ephem, datetime

today = datetime.date.today().strftime('%Y/%m/%d')

spring_equinox = '2024/03/19' # days back to +12hr after here
ss_mid = '2024/05/05'
summer_solstice = '2024/06/20' # longest day
sf_mid = '2024/08/05'
fall_equinox = '2024/09/22' # days get are -12hrs after here
fw_mid = '2024/11/07'
winter_solstice = '2024/12/21' # shortest day

days = [today, spring_equinox, ss_mid, summer_solstice, sf_mid, fall_equinox, fw_mid, winter_solstice]

# static latitude eg. equator, 23.26, 66.34
# for i in range(8):
#     day = days[i]
#
#     # print rise and set, change longitude by 10 from +90 to -90
#     print(day)
#     for lon in range(180, -180, -10):
#         # lat = 0 # equator
#         # lat = 23.2622 # tropic of cancer
#         lat = 38.3458 # mediterranean
#         # lat = 66.3339 # arctic circle
#
#         try:
#             result = getSunInfoSingle(lat, lon, day)
#             # list structure [date, sunrise, midday, sunset, total_hours]
#             print(lat, lon, result[1], result[3], result[4])
#         except (ephem.NeverUpError, ephem.AlwaysUpError) as e:
#             print(lat, lon, e)

#     # observations:
#     # repeating triplets pattern in sunrise when changing longitude
#     # equator = constant daylight 12 hours regardless of time of year give or take a min or two
#     # tropic of cancer = ~10h42m(shortest day) to ~13h35m(longest day)
#     # arctic circle = ~(shortest day) to ~(longest day)


# # static longitude eg. Miami, prime meridian, Singapore
# for i in range(8):
#     day = days[i]
#
#     # print rise and set, change latitude by 10 from +90 to -90
#     print(day)
#     for lat in range(90, -91, -10):
#         # lon = 0 # prime meridian
#         # lon = -80.1918 # Miami
#         lon = 103.8198 # Singapore
#
#         try:
#             result = getSunInfoSingle(lat, lon, day)
#             # list structure [date, sunrise, midday, sunset, total_hours]
#             print(lat, lon, result[1], result[3], result[4])
#         except (ephem.NeverUpError, ephem.AlwaysUpError) as e:
#             print(lat, lon, e)
#
#     # observations:
#     # no change whatsoever as longitude is changed
#     # around 12 hours all accross the board at both equinoxes
#     # after spring equinox north days get long and south days get short
#     # after fall equinox north days get short and south days get long

# show change of the year for certain areas
lat = 3.8617
lon = 11.5202
print('Yaounde')

for i in range(8):
    day = days[i]

    print(day)
    try:
        result = getSunInfoSingle(lat, lon, day)
        # list structure [date, sunrise, midday, sunset, total_hours]
        print(lat, lon, result[1], result[3], result[4])
    except (ephem.NeverUpError, ephem.AlwaysUpError) as e:
        print(lat, lon, e)
