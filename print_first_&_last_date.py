from datetime import datetime
florida_hurricane_dates = [
  datetime(2026, 5, 3),
  datetime(2023, 6, 15),
  datetime(2023, 4, 9),
  datetime(2025, 7, 21),
  datetime(2023, 5, 30)
]


# print the first and last date in the above list its ok.
print(florida_hurricane_dates[0])
print(florida_hurricane_dates[-1])

# sort the list which contain several dates.
ls=sorted(florida_hurricane_dates)

# Print the first and last ordered dates
print(ls[0])
print(ls[-1])