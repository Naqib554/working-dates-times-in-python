from datetime import datetime
onebike_datetimes = [
    '2023-06-20 09:30:00',
    '2023-06-20 11:45:00',
    '2023-06-20 14:20:00',
    '2023-06-20 17:10:00',
    '2023-06-20 20:05:00'
]


# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}

# Loop over all trips
for trip in onebike_datetimes:
    # Convert the datetime string to a datetime object
    trip_datetime = datetime.strptime(trip, '%Y-%m-%d %H:%M:%S')

    # Check to see if the trip starts before noon
    if trip_datetime.hour < 12:
        # Increment the counter for before noon
        trip_counts['AM'] += 1
    else:
        # Increment the counter for after noon
        trip_counts['PM'] += 1

print(trip_counts)




