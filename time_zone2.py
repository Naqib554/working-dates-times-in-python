from datetime import datetime, timedelta, timezone

onebike_datetime_strings = [
    ("2023-06-19 08:30:00", "2023-06-19 08:45:00"),
    ("2023-06-19 09:15:00", "2023-06-19 09:30:00")
]

# Create a timezone object corresponding to UTC-4
edt = timezone(timedelta(hours=-4))

# Loop over trips, updating the start and end datetimes to be in UTC-4
updated_trips = []
for trip in onebike_datetime_strings:
    start_dt = datetime.fromisoformat(trip[0])
    end_dt = datetime.fromisoformat(trip[1])
    # the bellow 2 lines return the new datetime objects with the updated timezone information.
    updated_start_dt = start_dt.replace(tzinfo=timezone.utc).astimezone(edt)
    updated_end_dt = end_dt.replace(tzinfo=timezone.utc).astimezone(edt)
    # now add the updated_start_dt and updated_end_dt to the updated_trips.
    updated_trips.append((updated_start_dt, updated_end_dt))
print(updated_trips)
# Print the updated trips
for trip in updated_trips:
    print(trip)
