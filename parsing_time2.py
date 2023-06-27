from datetime import datetime
# Write down the format string
fmt = "%Y-%m-%d %H:%M:%S"

# create a list tuple
onebike_datetime_strings = [
    ("2023-06-19 08:30:00", "2023-06-19 08:45:00"),
    ("2023-06-19 09:15:00", "2023-06-19 09:30:00")
]

# Initialize a list for holding the pairs of datetime objects
onebike_datetimes = []

# Loop over all trips
for (start, end) in onebike_datetime_strings:
#   this line create a dictionary called trip.
  trip = {'start': datetime.strptime(start, fmt),
          'end': datetime.strptime(end, fmt)}
  
  # Append the trip
  onebike_datetimes.append(trip)
print(onebike_datetimes)  

total_elapsed_time=sum()




# Pull out the start of the first trip
first_start = onebike_datetimes[0]['start']
# print(first_start)
# Format to feed to strftime()
fmt = "%Y-%m-%dT%H:%M:%S"

# Print out date with .isoformat(), then with .strftime() to compare
print(first_start.isoformat())
print(first_start.strftime(fmt))