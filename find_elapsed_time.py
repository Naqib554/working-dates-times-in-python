# To find out the elapsed time between multiple list of tuple
# where each consists two parst start_time and end_time.
from datetime import datetime

onebike_datetime_strings = [
    ("2023-06-19 08:30:00", "2023-06-19 08:45:00"),
    ("2023-06-19 09:15:00", "2023-06-19 09:50:00")
]

for trip in onebike_datetime_strings:
    dt_start = datetime.strptime(trip[0], "%Y-%m-%d %H:%M:%S")
    dt_end = datetime.strptime(trip[1], "%Y-%m-%d %H:%M:%S")
    
    total_elapsed_time = dt_end - dt_start
    print(total_elapsed_time)
    # # Get the total elapsed seconds in elapsed_time
    nw=total_elapsed_time.total_seconds()
    print(nw)


# find out the  short trip and long trip in list of trips.
short_trip=min(onebike_datetime_strings)
long_trip=max(onebike_datetime_strings)
print("The shortest trip was",str(short_trip))
print(long_trip)


# find out number of trips
number_of_trips=len(onebike_datetime_strings)
print(f"there are {number_of_trips} trips")

# find out the average length of trips.
average_trip_length=total_elapsed_time/number_of_trips
print(average_trip_length)