from datetime import date
# Create a date object for August 24, 1992.
date_object=date(1992,8,25)
print(type(date_object))
print(date_object)


# now ask python what day of the week
# remember that Python counts days of the week starting
# from Monday as 0, Tuesday as 1, and so on
# there are several attributes of datetime object
print(date_object.weekday())


# Great! Using the above same pattern, you could do more complex
# counting by using .day, .year, .weekday(), and so on