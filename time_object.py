from datetime import date
# Create a date object for August 24, 1992.
date_object=date(1992,8,25)
print(type(date_object))
print(date_object)


# now ask python what day of the week
# remember that Python counts days of the week starting
# from Monday as 0, Tuesday as 1, and so on
print(date_object.weekday())