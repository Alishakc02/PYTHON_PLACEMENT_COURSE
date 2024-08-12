#Python program to print current date and time
from datetime import datetime

#datetime object (now) containing current 
# date and time
now = datetime.now()
 
print("now =", now)

#dd/mm/YY H:M:S
date_time = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", date_time)