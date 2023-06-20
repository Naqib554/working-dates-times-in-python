from datetime import datetime

florida_hurricane_dates = [
  datetime(2023, 5, 3),
  datetime(2023, 6, 15),
  datetime(2023, 4, 9),
  datetime(2023, 7, 21),
  datetime(2023, 5, 30)
]

early_hurricanes = 0

for hurricane in florida_hurricane_dates:
#   6 represent the june month.
  if hurricane.month < 6:
    # The purpose of adding 1 to early_hurricanes in the loop is
    # to count the number of hurricanes that occurred before June 1.
    early_hurricanes += 1

print("Number of hurricanes before June 1:", early_hurricanes)
print("Florida hurricane dates:", florida_hurricane_dates)
