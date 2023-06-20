# Import date
from datetime import date

# Create a date object
andrew = date(1992, 8, 26)

# repsenting dates in different formates.
# like the bellow 
# Print the date in the format 'YYYY-MM'
print(andrew.strftime('%Y-%m'))
print(andrew.strftime('%Y'))
print(andrew.strftime('%m'))