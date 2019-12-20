import datetime as dt
import pytz as tz

d1= dt.datetime.now()

print (d1)
print (d1.month)
print (d1.year)
print (d1.day)

print(d1.strftime("%c"))
print(d1.strftime("%X"))
print(d1.strftime("%x"))
print(d1.strftime("%a"))
print(d1.strftime("%A"))

# Create a date with values
x = dt.datetime(2018, 4, 12)
print(x)


print (tz.all_timezones)
aus_date = dt.datetime.now(tz.timezone('US/Eastern'))
print (aus_date )


