# Import datetime
from datetime import datetime

# Create a datetime object
# The datetime constructor takes the year, month, day, hour, minute, second, 
# and a tzinfo argument to specify the timezone.
dt = datetime(2017, 10, 1, 15, 26, 26)

# Print the results in ISO 8601 format
print(dt.isoformat())

# Create a new datetime by replacing the year in dt with 1917 (instead of 2017)
df=dt.replace(year=1917)
print(df)
