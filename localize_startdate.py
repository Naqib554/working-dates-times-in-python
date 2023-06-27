# localize means assign the time zone information to the given datetime values.
# timezone: timezone is the area of earth that share the standard time.
import pandas as pd

# Sample DataFrame
rides = pd.DataFrame({
    'Start date': pd.to_datetime(['2023-06-26 10:00:00', '2023-06-27 15:30:00', '2023-06-28 08:45:00']),
    'Duration': [30, 45, 60],
    'Distance': [5.2, 7.8, 10.5]
})

# Localize the Start date column to America/New_York
# To avoid the ambigous datetime values we used to the default perameter ambigous='NaT'
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', ambiguous='NaT')


# Print first value
print(rides['Start date'].iloc[0])

# Convert the Start date column to Europe/London timezone.
rides['Start date']=rides['Start date'].dt.tz_localize('Europe/London', ambiguous='NaT')
print(rides['Start date'].iloc[0])