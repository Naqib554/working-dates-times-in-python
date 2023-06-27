from datetime import datetime

onebike_datetime_strings = [
    ("2023-06-19 08:30:00", "2023-06-19 08:45:00"),
    ("2023-06-19 09:15:00", "2023-06-19 09:30:00")
]

trip_length_seconds = 0  # Initialize the variable outside the loop

for trip in onebike_datetime_strings:
    trip_start = datetime.strptime(trip[0], "%Y-%m-%d %H:%M:%S")
    trip_end = datetime.strptime(trip[1], "%Y-%m-%d %H:%M:%S")
    
    trip_duration = trip_end - trip_start
    trip_length_seconds += trip_duration.total_seconds()

print('the total seconds of elapsed timem is :',trip_length_seconds)





# Success! Remember that timedelta objects are represented in Python as a number of days
# and seconds of elapsed time. Be careful not to use .seconds on a timedelta
# object, since you'll just get the number of sec