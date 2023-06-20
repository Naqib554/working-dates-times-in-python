from datetime import datetime
florida_hurricane_dates = [
  datetime(2026, 5, 3),
  datetime(2023, 6, 15),
  datetime(2023, 4, 9),
  datetime(2025, 7, 21),
  datetime(2023, 5, 30)
]


# Assign the earliest date to first_date
first_date =max(florida_hurricane_dates)

# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.isoformat()
us = "Our earliest hurricane date: " + first_date.strftime("%m/%d/%Y")

print("ISO: " + iso)
print("US: " + us)
