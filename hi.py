import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Start date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01'],
}
rides = pd.DataFrame(data)

# Convert 'Start date' column to datetime
rides['Start date'] = pd.to_datetime(rides['Start date'])

# Resample rides to monthly, take the size, plot the results
rides.resample('M', on='Start date') \
    .size() \
    .plot(ylim=[0, 100])

# Show the plot
plt.show()


# Overall, the resample() function is a powerful tool for manipulating and
# summarizing time series data at different frequencies.
