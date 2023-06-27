import pandas as pd

# Create a sample DataFrame
data = {
    'Start date': pd.to_datetime(['2023-06-20', '2023-06-21', '2023-06-22', '2023-06-23', '2023-06-24']),
    'Duration': [15, 20, 25, 30, 35]
}

rides = pd.DataFrame(data)

# Add a column for the weekday of the start date column in rides Dataframe.
# dt.day_name() return week_day name for each individual date in the dataframe.
rides['Ride start weekday'] = rides['Start date'].dt.day_name()
print(rides)
# this line of code return the median duration for each week day.
print(rides.groupby('Ride start weekday')['Duration'].median())
