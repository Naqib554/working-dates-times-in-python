import pandas as pd

# Create a sample DataFrame
data = {
    'Start station': ['A', 'B', 'C', 'D', 'E'],
    'End station': ['A', 'F', 'C', 'D', 'E'],
    'Duration': [120, 180, 90, 240, 150]
}
rides = pd.DataFrame(data)
# print(rides)
# Create joyrides
# the true values is the joyrides values.
joyrides = (rides['Start station'] == rides['End station'])
# print(joyrides)
# # Total number of joyrides

# after calculating the joyrides.sum() values the format() will replace 
# these values by curly braces in the string.
print("{} rides were joyrides".format(joyrides.sum()))

# # Median of all rides
print("The median duration overall was {:.2f} seconds".format(rides['Duration'].median()))

# # Median of joyrides
print("The median duration for joyrides was {:.2f} seconds".format(rides[joyrides]['Duration'].median()))
