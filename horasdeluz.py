from datetime import datetime, timedelta
import ephem, pgeocode, pytz, timezonefinder

# convert zip code single date
def getSunInfoSingleZip(zip_code, day):
    nomi = pgeocode.Nominatim("us")
    location = nomi.query_postal_code(zip_code)

    lat = location["latitude"]
    lon = location["longitude"]
    return getSunInfoSingle(lat, lon, day)

# convert zip code for date range
def getSunInfoRangeZip(zip_code, start, end):
    nomi = pgeocode.Nominatim("us")
    location = nomi.query_postal_code(zip_code)

    lat = location["latitude"]
    lon = location["longitude"]
    return getSunInfoRange(lat, lon, start, end)

# return array of format [date, sunrise, midday, sunset, total_hours]
def getSunInfoSingle(lat, lon, day):
    sunrise_dt, sunset_dt = get_sunrise_sunset(lat, lon, day)

    sunrise_time = sunrise_dt.strftime("%H:%M")
    sunset_time = sunset_dt.strftime("%H:%M")

    total_hours, midday = findDayLengthAndMiddayHour(sunrise_time, sunset_time)

    return [day, sunrise_time, midday, sunset_time, total_hours]

# return 2d array of [date, sunrise, midday, sunset, total_hours] for each date in range
def getSunInfoRange(lat, lon, start_date, end_date):
    start = datetime.strptime(start_date, "%Y/%m/%d")
    end = datetime.strptime(end_date, "%Y/%m/%d")

    day_range = []
    for i in range((end - start).days + 1):
        day = start + timedelta(days=i)
        sunrise_dt, sunset_dt = get_sunrise_sunset(lat, lon, day)

        sunrise_time = sunrise_dt.strftime("%H:%M")
        sunset_time = sunset_dt.strftime("%H:%M")

        total_hours, midday = findDayLengthAndMiddayHour(sunrise_time, sunset_time)

        day_range.append([day, sunrise_time, midday, sunset_time, total_hours])

    return day_range

# returns total hours of daylight and true midday given a sunrise and sunset
def findDayLengthAndMiddayHour(sunrise, sunset):
    dt_rise = datetime.strptime(sunrise, "%H:%M")
    dt_set = datetime.strptime(sunset, "%H:%M")

    midday_hour = (dt_set - dt_rise) / 2

    daylen = (dt_set - dt_rise)
    midday = (dt_rise + midday_hour).strftime("%H:%M")

    return [daylen, midday]

# returns a the sunrise and sunset times for a given location in its respective timezone
def get_sunrise_sunset(lat, lon, date):
    observer = ephem.Observer()
    observer.lat = str(lat)
    observer.lon = str(lon)
    observer.date = date

    sunrise = observer.next_rising(ephem.Sun())
    sunset = observer.next_setting(ephem.Sun())

    tf = timezonefinder.TimezoneFinder()
    timezone_str = tf.certain_timezone_at(lat=lat, lng=lon)
    timezone = pytz.timezone(timezone_str)
    dt = datetime.now()

    return sunrise.datetime() + timezone.utcoffset(dt), sunset.datetime() + timezone.utcoffset(dt)

def getConsoleInput():
    response1 = input("Are you in the united states? (y/n): ").lower()

    if response1[0] == "y":
        zip_code = input("Enter your zip code: ")
        nomi = pgeocode.Nominatim("us")
        location = nomi.query_postal_code(zip_code)

        lat = location["latitude"]
        lon = location["longitude"]
    else:
        lat = float(input("Please enter your latitude: "))
        lon = float(input("Please enter your longitude: "))

    qty = input("Would you like to calculate for a single date or a range of dates? (s/r): ")
    if qty[0] == "r":
        start_date = input("Enter start date (YYYY/MM/DD): ")
        end_date = input("Enter end date (YYYY/MM/DD): ")

        startd = datetime.strptime(start_date, "%Y/%m/%d")
        endd = datetime.strptime(end_date, "%Y/%m/%d")

        for i in range((endd-startd).days + 1):
            day = startd + timedelta(days = i)
            sunrise_dt, sunset_dt = get_sunrise_sunset(lat, lon, day)

            sunrise_time = sunrise_dt.strftime("%H:%M")
            sunset_time = sunset_dt.strftime("%H:%M")

            daylen, midday = findDayLengthAndMiddayHour(sunrise_time, sunset_time)

            print("date\t=\t%s\nsunrise\t=\t%s\nmidday\t=\t%s\nsunset\t=\t%s" % (day, sunrise_time, midday, sunset_time))
            print("total hours o daylight = %s" % (daylen))
        print("peace be upon you")

    else:
        date = input("Enter a date (YYYY/MM/DD): ")
        sunrise_dt, sunset_dt = get_sunrise_sunset(lat, lon, date)

        sunrise_time = sunrise_dt.strftime("%H:%M")
        sunset_time = sunset_dt.strftime("%H:%M")

        daylen, midday = findDayLengthAndMiddayHour(sunrise_time, sunset_time)

        print("date\t=\t%s\nsunrise\t=\t%s\nmidday\t=\t%s\nsunset\t=\t%s" % (date, sunrise_time, midday, sunset_time))
        print("total hours o daylight = %s" % (daylen))
        print("peace be upon you")

# getConsoleInput() # <---- (un)comment this line to toggle console input




