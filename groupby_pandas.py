import pandas as pd

# Sample data for the DataFrame
data = {
    'Start date': pd.date_range(start='2023-01-01', periods=180, freq='D'),
    'Member type': ['A', 'B'] * 90,
    'Duration': [10, 15] * 90
}

# Create the DataFrame
rides = pd.DataFrame(data)
# print(rides)
# Convert 'Start date' column to datetime if it's not already in datetime format
rides['Start date'] = pd.to_datetime(rides['Start date'])
# print(rides['Start date'])

# Group rides by 'Member type' and resample to the month
grouped = rides.groupby('Member type').resample('M', on='Start date')
print(grouped)

# # Calculate the median duration for each group
median_duration = grouped['Duration'].median()

# # Print the median duration for each group
print(median_duration)


# However, when printing the median_duration variable, 
# you should see the actual median duration values for each group.