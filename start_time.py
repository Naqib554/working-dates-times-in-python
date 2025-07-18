#March 29, throughout a decade
# Daylight Saving rules are complicated: they're different in different places, they change over time,
# and they usually start on a Sunday (and so they move around the calendar).


# Let's look at the UTC offset for March 29, 
# at midnight, for the years 2000 to 2010.

# Import datetime and tz
from datetime import datetime
from dateutil import tz

# Create starting date
dt = datetime(2000, 3, 29, tzinfo = tz.gettz('Europe/London'))
# print(dt)
# Loop over the dates, replacing the year, and print the ISO timestamp
for y in range(2000, 2011):
  print(dt.replace(year=y).isoformat())
