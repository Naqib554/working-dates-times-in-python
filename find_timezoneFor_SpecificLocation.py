# Import tz
from dateutil import tz
from datetime import datetime

onebike_datetime_strings = [
    ("2023-06-19 08:30:00", "2023-06-19 08:45:00"),
    ("2023-06-19 09:15:00", "2023-06-19 09:50:00")
]

timezone=[]
# Create a timezone object for Eastern Time
# tz.getz() is used to retrive the time zone information 
# for a specific location .
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetime_strings[:10]:

  start_dt=datetime.strptime(trip[0],'%Y-%m-%d %H:%M:%S')
  end_dt=datetime.strptime(trip[1],'%Y-%m-%d %H:%M:%S')
#   print(start_dt)
  #   we create two aware datetime object bellow
  start_dt=start_dt.replace(tzinfo=et)
  end_dt=end_dt.replace(tzinfo=et)
  timezone.append(start_dt)
  timezone.append(end_dt)
# print(timezone)


# Create the timezone object
uk = tz.gettz('Europe/London')
# pull the start of the first trip.
local=timezone[0]
# print(local)
# When you need to move a datetime from one timezone into another, use .astimezone()
notlocal=local.astimezone(uk)
print(local.isoformat())
print(notlocal.isoformat())


