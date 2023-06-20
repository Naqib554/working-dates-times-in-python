from datetime import datetime
florida_hurricane_dates = [
  datetime(2023, 5, 3),
  datetime(2023, 6, 15),
  datetime(2023, 4, 9),
  datetime(2023, 7, 21),
  datetime(2023, 5, 30)
]

# A dictionary to count hurricanes per calendar month
hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6:0,
		  				 7: 0, 8:0, 9:0, 10:0, 11:0, 12:0}

# Loop over all hurricanes
for hurricane in florida_hurricane_dates:
  # Pull out the month
  month = hurricane.month
#   print(month)
  # Increment the count in your dictionary by one
  hurricanes_each_month[month] += 1
  
print(hurricanes_each_month)




# Success! This illustrated a generally useful pattern for working with complex data: creating a dictionary,
# performing some operation on each element, and storing the results back in the dictionary.


