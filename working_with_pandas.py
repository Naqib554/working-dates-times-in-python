import pandas as pd

# Sample dataframe
rides = pd.DataFrame({
    'Start date': pd.to_datetime(['2023-01-01', '2023-02-05', '2023-03-10', '2023-04-15']),
    'End date': pd.to_datetime(['2023-01-03', '2023-02-08', '2023-03-15', '2023-04-20'])
})
print(rides)
# The line rides['End date'].shift(1) shifts the values in the 'End date' column by one position,
# effectively bringing the end date of the previous ride to the current
# ride's row. Since there is no previous ride for the first row, it results in a missing value represented as NaT (Not a Time)
# Calculate the difference in start date and end date of the previous row
# For the second row, this calculation is performed as follows:
# Start date of the second row: '2023-02-05'
# End date of the first row (shifted value): '2023-01-03'
# Difference: '2023-02-05' - '2023-01-03' = 33 days
# Similarly, the calculations are performed for the subsequent rows, 
rides['Time since'] = rides['Start date'] - rides['End date'].shift(1)


# # Convert timedelta to seconds
rides['Time since'] = rides['Time since'].dt.total_seconds()

print(rides['Time since'])
# # Resample to monthly buckets according to start date
monthly = rides.resample('M', on='Start date').mean()

# # Calculate the average hours between rides each month
monthly['Time since'] = monthly['Time since'] / (60 * 60)

# # Print the resulting dataframe
print(monthly)
