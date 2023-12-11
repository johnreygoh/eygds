# date time
import datetime

dateref = datetime.datetime.now()
print(dateref)

d = dateref.strftime("%d/%m/%Y")
print(dateref.strftime("%m %b %B"))
print(dateref.strftime("%d %a %A %D"))
print(dateref.strftime("%H:%M:%S"))
print(dateref.strftime("%B %d,%Y (%A)"))

# date interval / difference
startdate = datetime.datetime.strptime("13/10/1965","%d/%m/%Y")
enddate = dateref

# difference in years
years = enddate - startdate
print(years.days/365)









