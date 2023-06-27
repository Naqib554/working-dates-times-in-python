# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('datetime.csv',
  parse_dates = ['start_date','end_date'])

rides_duration=rides['start_date']-rides['end_date']
# print(rides_duration)
rides['duration']=rides_duration.dt.total_seconds()
print(rides['duration'])

# Print the initial (0th) row
print(rides.iloc[0])



# Great! Because Pandas supports method chaining, you could also perform this operation in one line:
# rides['Duration'] = (rides['End date'] - rides['Start date']).dt.total_seconds()

