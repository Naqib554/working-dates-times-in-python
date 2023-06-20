# it is a question where you can find the number of days
# between two different dates.

# Import date
from datetime import date

# Create a date object for May 9th, 2007
start = date(2007, 5, 9)

# Create a date object for December 13th, 2007
end = date(2007, 12, 13)

# Subtract the two dates and print the number of days
print((end - start).days)


#  One thing to note: be careful using this technique for historical dates hundreds of years in the past. Our calendar systems have changed over time, 
# and not every date from then would be the same day and month today.