from datetime import datetime, timezone

onebike_datetime_strings = [
    ("2023-06-19 08:30:00", "2023-06-19 08:45:00"),
    ("2023-06-19 09:15:00", "2023-06-19 09:50:00")
]

for i in onebike_datetime_strings:
    start_dt = datetime.fromisoformat(i[0])
    # print(start_dt)
    utc_time = start_dt.astimezone(timezone.utc)
    print(utc_time)


# This code will iterate over the onebike_datetime_strings list,
# convert the start datetime string to a datetime object using datetime.fromisoformat(),
# and then convert it to UTC using astimezone(timezone.utc).
# The resulting UTC datetime objects will be printed for each iteration.