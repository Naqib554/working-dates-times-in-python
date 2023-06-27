import pandas as pd

# Sample data for the DataFrame
data = {
    'Start date': pd.date_range(start='2023-01-01', periods=180, freq='D'),
    'Member type': ['A', 'B'] * 90,
    'Duration': [10, 15] * 90
}

# Create the DataFrame
rides = pd.DataFrame(data)

# Convert 'Start date' column to datetime if it's not already in datetime format
rides['Start date'] = pd.to_datetime(rides['Start date'])

# Group rides by 'Member type' and resample to the month
# resample()  allows you to aggregate data over different time intervals.
#  uses .resample('M') to group the rides by month. This means that the data will be aggregated and
# grouped on a monthly basis. The resulting grouped object is a DatetimeIndexResamplerGroupby object.
grouped = rides.groupby('Member type').resample('M', on='Start date')

# Calculate the median duration for each group
median_duration = grouped['Duration'].median()

# Print the median duration for each group
print(median_duration)
