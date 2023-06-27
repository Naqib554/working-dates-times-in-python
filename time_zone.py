# Import datetime, timezone
from datetime import datetime, timezone

# October 1, 2017 at 15:26:26, UTC
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=timezone.utc)

# Print results
print(dt.isoformat())






# In the datetime module, the timezone.utc object is a predefined time zone object that represents
# the UTC time zone, which is a standard time reference used worldwide. By using tzinfo=timezone.utc,
# you are assigning the UTC time zone to the datetime object dt
# Therefore, the resulting dt object represents the date and time
# "October 1, 2017, at 15:26:26" in the UTC time zone.