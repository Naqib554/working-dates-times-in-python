# Import datetime, timedelta, timezone
from datetime import datetime, timedelta, timezone
# these 3 classes work with date,time and timezone.

# Create a timezone object for Pacific Standard Time, or UTC-8
pst = timezone(timedelta(hours=-8))
print(pst)

# October 1, 2017 at 15:26:26, UTC-8
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=pst)


# Print results
print(dt.isoformat())