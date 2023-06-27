# When we compare times in local time zones, everything gets converted into clock time.
#  Remember if you want to get absolute time differences, always move to UTC!

from datetime import datetime, timedelta, timezone
from dateutil import tz

# Define a list of time intervals
time_intervals = [
    ("2017-03-12T00:00:00-05:00", "2017-03-12T06:00:00-04:00"),
    ("2022-08-15T08:30:00+02:00", "2022-08-15T16:45:00+02:00"),
    ("2023-01-01T12:00:00-08:00", "2023-01-01T18:30:00-08:00")
]

# uk = tz.gettz('Europe/London')
# Iterate through the list of time intervals
for interval in time_intervals:
    start_time = datetime.fromisoformat(interval[0])
    end_time = datetime.fromisoformat(interval[1])
    start_time=start_time.replace(tzinfo=timezone.utc)
    end_time=end_time.replace(tzinfo=timezone.utc)


    # Calculate the duration in hours
    duration = (end_time - start_time).total_seconds() / (60 * 60)

    # Print the interval and its duration
    print("Interval:", interval[0], "to", interval[1])
    print("Duration (hours):", duration)
    print()
