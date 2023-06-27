from datetime import datetime
s='2002-8-3'
fmt='%Y-%m-%d'

obj_datetime=datetime.strptime(s,fmt)
print(obj_datetime)